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

while True:
    Timeupdate=dt.datetime.now()
    if(Timeupdate.minute%3==0):
        msg=Timeupdate
        r = requests.post(url, headers=headers , data = {'message':msg})

        
        
        
    time.sleep(40)
                    
     
