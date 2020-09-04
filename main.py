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
from io import BytesIO

url = 'https://notify-api.line.me/api/notify'
token = environ['token']
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}




r = requests.get(environ['ggsh'])
'''
data = r.content

df_slot1=pd.read_excel(BytesIO(data),sheet_name='Slot1')
df_slot2=pd.read_excel(BytesIO(data),sheet_name='Slot2')
#df=df.set_index('Time')
d_slot1=df_slot1.to_dict('split')
d_slot2=df_slot2.to_dict('split')
'''

while True:
    Timeupdate=dt.datetime.now()
    if(Timeupdate.minute%3==0):
        msg=r
        r = requests.post(url, headers=headers , data = {'message':msg})

        
        
        
    time.sleep(40)
                    
     
