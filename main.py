import tweepy
from tweepy import OAuthHandler
from tweepy import API
import json
import datetime as dt
import  time

url = 'https://notify-api.line.me/api/notify'
token = environ['token']
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
msg ='Program runnning'
r = requests.post(url, headers=headers , data = {'message':msg})


access_token=environ['access_token']
access_token_secret=environ['access_token_secret']
consumer_key=environ['consumer_key']
consumer_secret=environ['consumer_secret']
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)


def trend_twitter():  #ดึงข้อมูล Trends Twitter
    brazil_trends=api.trends_place(1118370)
    trends = json.loads(json.dumps(brazil_trends, indent=1))
    
    Name_trend=[]
    tweet_volume=[]
    for i in trends[0]["trends"]:
        if '#' in i["name"]:
            Name_trend.append(i["name"]) 
            tweet_volume.append(i["tweet_volume"])    
           
    return(Name_trend,tweet_volume)

def top10(trend_text,A,B): #top n value 
    trend_plot=[]

    text='Top Trends Japan '+Time
    for i in range(A,B):
        text=text+'\n'+str(i+1)+') '+trend_text[i]
        trend_plot.append(trend_text[i])
    text=text
    return(text)
    

while True:
    Timeupdate=dt.datetime.now()
    if(Timeupdate.minute==46 or Timeupdate.minute==26)
    Time=str(Timeupdate.strftime("%x"))+'  '+str(Timeupdate.strftime("%X"))
    trend_text=trend_twitter()
    text1=top10(trend_text[0],0,5)
    api.update_status(status=text1)
    text2=top10(trend_text[0],6,10)
    time.sleep(40)
    api.update_status(status=text2)
    time.sleep(40)



