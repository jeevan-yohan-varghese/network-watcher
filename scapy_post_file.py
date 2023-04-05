from scapy.all import *
import re
from datetime import datetime
import gen_report
def sniff_http_post(pkt):
    shouldWrite=False
    mFileName=""
    mDest=""
    
    if pkt.haslayer(TCP) and pkt.haslayer(Raw):
        raw_data = pkt[Raw].load.decode("utf-8", errors="ignore")
        # Check for HTTP POST request
        if re.search(r"(POST|post) /(.*?) HTTP/1", raw_data):
            # Check for multipart/form-data content type
            if "Content-Type: multipart/form-data;" in raw_data:
                # Extract the filename, path and file type being sent
                match = re.search(r"Content-Disposition: form-data; name=\".*?\"; filename=\"(.*?)\"", raw_data)
                if match:
                    filename = match.group(1)
                    filepath = re.search(r"Content-Disposition: form-data; name=\"(.*?)\"; filename", raw_data).group(1)
                    file_type = re.search(r"\.(.*?)$", filename).group(1)
                    print(f"File: {filepath}/{filename}")
                    print(f"File type: {file_type}")
                    mFileName=filename
                    shouldWrite=True
            # Extract the destination URL
            dest_url = re.search(r"Host: (.*?)\r\n", raw_data)
            if dest_url:
                mDest=dest_url.group(1)
                print(f"Destination URL: {dest_url.group(1)}")
            # Extract the response status
            res_status = re.search(r"HTTP/\d\.\d (\d{3})", raw_data)
            if res_status:
                print(f"Response status: {res_status.group(1)}")
            if shouldWrite:
                now = datetime.now()
 
                #print("now =", now)

                # dd/mm/YY H:M:S
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                #print("date and time =", dt_string)
                gen_report.write_html( {"file":[mFileName],"date":[dt_string],"url":[mDest]}) 
# Sniff packets on interface "eth0"
sniff(filter="tcp port 80", prn=sniff_http_post)
