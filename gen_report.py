from jinja2 import Environment, FileSystemLoader
import os
import pandas as pd
root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment( loader = FileSystemLoader(templates_dir) )
template = env.get_template('template.html')
 



def write_html(current_file):
    
    df=pd.DataFrame()
    try:
      
        df = pd.read_csv('data/records.csv')
    except pd.errors.EmptyDataError:
        print('File is empty')
    else:
        df.columns=["file","date","url"]
    df_new=pd.DataFrame(current_file)
    frames = [df, df_new]
  
    
    df=pd.concat(frames)
    df.to_csv("data/records.csv",index=False)
    saved_items=df.to_dict('records')
    print(saved_items)
    with open('generated.html', 'w') as fh:
        fh.write(template.render(
            items=saved_items
        ))


# if __name__ == '__main__':
#     main()