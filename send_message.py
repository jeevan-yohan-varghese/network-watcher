
import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate("network_service_account.json")
firebase_admin.initialize_app(cred)

def send_token_push(title, body):
 mtokens=["e470jt9fSA-Ti4esTzF4k3:APA91bEmmTyWiLQGkOH6MxvJB7v8bcsni5Y4QJJAJbfi1an6aw03ZjmYT_sAU8a1K2sEKhE10QUQQuMEeL85BPQ2wI-nq8OBTu9AwNL1cLjqUgTHm2n6se17ga-d2JCQc0iU_gqbR5Rs"]
 print("Sending...")
 message = messaging.MulticastMessage(
   notification=messaging.Notification(
   title=title,
   body=body
  ),
  tokens=mtokens
 )
 res=messaging.send_multicast(message)
 print(print('response', res.success_count, res.failure_count)
)

if __name__=='__main__':
  send_token_push("Test Python","test msg",["e470jt9fSA-Ti4esTzF4k3:APA91bEmmTyWiLQGkOH6MxvJB7v8bcsni5Y4QJJAJbfi1an6aw03ZjmYT_sAU8a1K2sEKhE10QUQQuMEeL85BPQ2wI-nq8OBTu9AwNL1cLjqUgTHm2n6se17ga-d2JCQc0iU_gqbR5Rs"])