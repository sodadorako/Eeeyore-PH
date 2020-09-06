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

file_name = 'https://docs.google.com/spreadsheet/ccc?key=19TWYLSwgC4cJe9mslepF1-et9RSP-C3VxQEtYxSS2yw&output=xlsx'
df_slot2 = pd.read_excel(file_name,sheet_name='Slot2')
df_slot1 = pd.read_excel(file_name,sheet_name='Slot1')

d_slot1=df_slot1.to_dict('split')
d_slot2=df_slot2.to_dict('split')


url = 'https://notify-api.line.me/api/notify'
token = environ['token']
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
msg ='Program runnning'
r = requests.post(url, headers=headers , data = {'message':msg})


while True:
    Timeupdate=dt.datetime.now()
    if(Timeupdate.minute==29 or Timeupdate.minute==10):
        Time=str(Timeupdate.strftime("%x"))+'  '+str(Timeupdate.strftime("%X"))
        if(Timeupdate.minute==29):
            timecheck=1
        elif(Timeupdate.minute==10):
            timecheck=2
        for i in d_slot1['data']:
            if(i[0]==Timeupdate.hour and i[1]==timecheck):
                Tweets_slot1=i[5]
        for i in d_slot2['data']:
            if(i[0]==Timeupdate.hour and i[1]==timecheck):
                Tweets_slot2=i[5]
        msg=Tweets_slot2
        r = requests.post(url, headers=headers , data = {'message':msg})
    time.sleep(40)
