import requests

url = 'https://notify-api.line.me/api/notify'
token = environ['token']
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

msg='hello'

r = requests.post(url, headers=headers , data = {'message':msg})

