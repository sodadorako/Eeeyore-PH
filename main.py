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
msg ='Program runnning'
r = requests.post(url, headers=headers , data = {'message':msg})

from datetime import tzinfo
msg ='Program runnning2'
r = requests.post(url, headers=headers , data = {'message':msg})

class FixedOffset(tzinfo):
    def __init__(self, offset):
        self.__offset = timedelta(hours=offset)
        self.__dst = timedelta(hours=offset-1)
        self.__name = ''

    def utcoffset(self, dt):
        return self.__offset

    def tzname(self, dt):
        return self.__name

    def dst(self, dt):
        return self.__dst

msg ='Program runnning3'
r = requests.post(url, headers=headers , data = {'message':msg})

Timeupdate=dt.datetime.now(FixedOffset(9))
msg =Timeupdate.hour
r = requests.post(url, headers=headers , data = {'message':msg})
