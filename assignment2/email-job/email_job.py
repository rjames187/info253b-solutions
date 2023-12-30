import os
import requests

def send_email(address):
  API_KEY = os.getenv('API_KEY')
  DOMAIN = os.getenv('DOMAIN')
  print(API_KEY, DOMAIN)
  print(address + ' is the address!')
  requests.post(
    f"https://api.mailgun.net/v3/{DOMAIN}/messages",
    auth=("api", API_KEY),
    data={"from": f"Task Application <mailgun@{DOMAIN}>",
          "to": [address],
          "subject": "Task Completed",
          "text": "Congratulations on Completing a task!"
          }
  )
  print('message sent to mailgun!')

