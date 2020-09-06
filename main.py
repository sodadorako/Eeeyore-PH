import tweepy
from tweepy import OAuthHandler
from tweepy import API
import datetime as dt
import  time
from os import environ
import json
from datetime import datetime,timedelta
import pandas as pd
import requests

url = 'https://notify-api.line.me/api/notify'
token = environ['token']
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
msg ='Program runnning111'
r = requests.post(url, headers=headers , data = {'message':msg})

time.sleep(10)

file_name = 'https://docs.google.com/spreadsheet/ccc?key=19TWYLSwgC4cJe9mslepF1-et9RSP-C3VxQEtYxSS2yw&output=xlsx'
df_slot2 = pd.read_excel(file_name,sheet_name='Slot2')
df_slot1 = pd.read_excel(file_name,sheet_name='Slot1')

url = 'https://notify-api.line.me/api/notify'
token = environ['token']
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
msg =df_slot2['Username'][0]
r = requests.post(url, headers=headers , data = {'message':msg})

