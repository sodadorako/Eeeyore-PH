import requests
from os import environ
import time


url = 'https://notify-api.line.me/api/notify'
token = environ['token']
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

while True:
    msg='hello'
    r = requests.post(url, headers=headers , data = {'message':msg})
    time.sleep(300)
