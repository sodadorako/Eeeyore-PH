

from os import environ
#import requests
import datetime as dt
#import tweepy
import  tweepy
from tweepy import OAuthHandler
from tweepy import API
#from tweepy import OAuthHandler
#from tweepy import API
import json


#from unittest import TestCase
import pandas as pd
import time
#import locale
import requests
#import datetime
from datetime import datetime,timedelta
import requests
from datetime import tzinfo, timedelta, datetime

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


url = 'https://notify-api.line.me/api/notify'
token = environ['token']
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}


msg ='Program runnning'


r = requests.post(url, headers=headers , data = {'message':msg})
from io import BytesIO


r = requests.get(environ['gurl'])
data = r.content

df_slot1=pd.read_excel(BytesIO(data),sheet_name='Slot1')
df_slot2=pd.read_excel(BytesIO(data),sheet_name='Slot2')
#df=df.set_index('Time')
d_slot1=df_slot1.to_dict('split')
d_slot2=df_slot2.to_dict('split')







url = 'https://notify-api.line.me/api/notify'
token = environ['token']
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

access_token=environ['access_token']
access_token_secret=environ['access_token_secret']
consumer_key=environ['consumer_key']
consumer_secret=environ['consumer_secret']
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

def twitter_data(Name,lang,Retweets):
    now = datetime.strftime(datetime.now()-timedelta(1),"%Y-%m-%d")
    now1 = datetime.strftime(datetime.now(),"%Y-%m-%d")
    #now=now.strftime("%Y-%m-%d")
    Data=list()
    try:
        for tweet in tweepy.Cursor(api.search,q=str(Name)+Retweets,count=1000,since=now,lang=lang).items():
            Data.append({'created_at':tweet.created_at,
                          'texts':tweet.text,
                     'id':tweet.id,
                     'source':tweet.source,
                     'geo':tweet.geo,
                     'lang':tweet.lang,
                      'Retweet':tweet.retweet_count,
                      'Favorite':tweet.favorite_count,
                      'id_str':tweet.id_str,
                      'place':tweet.place,
                      'entities':tweet.entities,
                      'Has':tweet.entities.get('hashtags'),
                      'followers_count':tweet.user.followers_count,
                      'protected':tweet.user.protected,
                      'description':tweet.user.description,
                      'name':tweet.user.screen_name,
                      'friends_count':tweet.user.friends_count,
                      'statuses_count':tweet.user.statuses_count,
                      'ids':tweet.user.id,
                      'location':tweet.user.location,
                      'profile_image_url':tweet.user.profile_image_url,
                      'join_date':tweet.user.created_at
                      
                 })
            #time.sleep(0.055)
        
    except tweepy.TweepError:
        time.sleep(10) # sleep for 2 minutes. You may try different time
        print('Maximum')
    df=pd.DataFrame(Data)
    df=df.set_index('created_at')
    df=df.tz_localize('Etc/GMT+9', level=0).tz_convert(None)
    df=df.reset_index()
    #print(df)
    df['today']=pd.Timestamp.today()
    df['age']=df['today']-df['join_date']
    df['dif_age']=df['age'].dt.days
    df['dif_age']=df['dif_age']/365
    df[df['created_at']==now1]
    print('dfcom')
    return(df,now)

def related_hashtag(df,text_has):
    hastag=[]
    #pd.DataFrame(k['fgfdgd'])
    for i in df['Has']:
        for items in i:
            hastag.append(items['text'].lower())
            #print(t['text'])

        
        df_hastag=pd.DataFrame({'#Hastag':hastag})
        df_hastag['Count']=1
        df_hastag=df_hastag.groupby(['#Hastag']).sum()
        df_hastag=df_hastag.sort_values(by=['Count'], ascending=False)
    df_hastag=df_hastag.head(4)
    df_hastag=df_hastag.tail(3)
    df_hastag=df_hastag.reset_index()
    #print(len(df_hastag))
    
    for i in range(0,len(df_hastag)):
        #print(df_hastag['#Hastag'][i])
        text_has=text_has+'\n'+str(i+1)+') '+'#'+str(df_hastag['#Hastag'][i])
    return(text_has)
    


def trend_twitter():  #ดึงข้อมูล Trends Twitter
    brazil_trends=api.trends_place(1118370)
    trends = json.loads(json.dumps(brazil_trends, indent=1))
    
    Name_trend=[]
    tweet_volume=[]
    for i in trends[0]["trends"]:
        if 'notghjhghj' not in i["name"]:
            Name_trend.append(i["name"]) 
            tweet_volume.append(i["tweet_volume"])    
           
    return(Name_trend,tweet_volume)

def top10(trend_text,A,B,ad): #top n value 
    trend_plot=[]
    value_plot=[]
    text='日本トレンド・ランキング '+Time
    for i in range(A,B):
        text=text+'\n'+str(i+1)+') '+trend_text[i]
        trend_plot.append(trend_text[i])
        value_plot.append(value_trend[i])
    text=text+'\n\n'+ad
    return(text,trend_plot,value_plot)





run=0

qqq=['#JUNGKOOK']
while run<3:
    Timeupdate=dt.datetime.now(FixedOffset(9))
    if(Timeupdate.minute==45 or Timeupdate.minute==15):

        Time=str(Timeupdate.strftime("%Y-%m-%d"))+'  '+str(Timeupdate.strftime("%X"))
        print(Time)
        
        
        if(Timeupdate.minute==15):
            timecheck=1
        elif(Timeupdate.minute==45):
            timecheck=2
        
        
        for i in d_slot1['data']:
            if(i[0]==Timeupdate.hour and i[1]==timecheck):
                print(i[5])
                Tweets_slot1=i[5]
                img_slot1=i[7]
                url_slot1=i[8]
        
        for i in d_slot2['data']:
            if(i[0]==Timeupdate.hour and i[1]==timecheck):
                print(i[5])
                Tweets_slot2=i[5]
                img_slot2=i[7]
                url_slot2=i[8]
        

        trend_text,value_trend=trend_twitter()
        text1,trend_plot1,value_plot1=top10(trend_text,0,5,Tweets_slot2)
        text0,trend_plot0,value_plot0=top10(trend_text,0,10,Tweets_slot2)
        text2,trend_plot2,value_plot2=top10(trend_text,5,10,Tweets_slot1)
        
        

        
        
        if(img_slot2==0):
            try:
                api.update_status(status=text1)
                print('Tweets Top Trends part 1 Success!')
                time.sleep(20)
            except:
                msg='lot2 Error   '+str(Time)
                r = requests.post(url, headers=headers , data = {'message':msg})
                time.sleep(20)
            #api.update_status(status=text2)
            #reply_last(text2)
            
        elif(img_slot2==1):
            try:
                api.update_status(status=text1,attachment_url=url_slot2)
                print('Tweets Top Trends part 1 Success!')
                time.sleep(20)
            except:
                msg='lot2 Error   '+str(Time)
                r = requests.post(url, headers=headers , data = {'message':msg})
                time.sleep(20)
            #api.update_status(status=text2)
            #reply_last(text2)

                
        else:
            try:
                media_ids=[]
                res = api.media_upload('C:/Users/Admin/Google Drive/Shared/'+str(img_slot2))
                media_ids.append(res.media_id)
                api.update_status(status=text1, media_ids=media_ids)
                print('Tweets Top Trends part 1 Success Photo !')
                time.sleep(20)
            except:
                msg='lot2 Error   '+str(Time)
                r = requests.post(url, headers=headers , data = {'message':msg})
                time.sleep(20)
            
            
            
            
        if(img_slot1==0):
            try:
                api.update_status(status=text2)
                print('Tweets Top Trends part 2 Success!')
                time.sleep(20)
                #api.update_status(status=text2)
                #reply_last(text2)
            except:
                msg='lot1 Error   '+str(Time)
                r = requests.post(url, headers=headers , data = {'message':msg})
                time.sleep(20)
            
        elif(img_slot1==1):
            try:
                api.update_status(status=text2,attachment_url=url_slot1)
                print('Tweets Top Trends part 1 Success!')
                time.sleep(20)
                #api.update_status(status=text2)
                #reply_last(text2)
            except:
                msg='lot1 Error   '+str(Time)
                r = requests.post(url, headers=headers , data = {'message':msg})
                time.sleep(20)
               
        else:
            try:
                media_ids=[]
                res = api.media_upload('C:/Users/Admin/Google Drive/Shared/'+str(img_slot1))
                media_ids.append(res.media_id)
                api.update_status(status=text2, media_ids=media_ids)
                print('Tweets Top Trends part 2 Success Photo !')
                time.sleep(20)
            except:
                msg='lot1 Error   '+str(Time)
                r = requests.post(url, headers=headers , data = {'message':msg})
                time.sleep(20)
        
        
        
        for i in trend_plot0:
            if i not in qqq:
                hashtag=i
                qqq.append(i)
                break
        
        print(hashtag)
        Retweets=" -filter:retweets"   #  " -filter:retweets"  ไม่รวม Retweet  , ""  รวม Retweet
        lang='' #'th' , 'en' , 'jp'  เว้นว่างสำหรับทุกภาษา 
        df,now=twitter_data(hashtag,lang,Retweets)
        #print(df)
        text_has=hashtag+' のデータ'+'   '+str(now)+'\nツイート   :  '+str(len(df))+'\nアカウント  :  '+str(df[['ids']].drop_duplicates().count()[0])+'\nリツイート  :  '+str(df['Retweet'].sum(axis = 0, skipna = True))+'\nいいねの数  :  '+str(df['Favorite'].sum(axis = 0, skipna = True))+'\n関連ハッシュタグ・トップ3'
        df_has=related_hashtag(df,text_has)
         
        
        time.sleep(60)
    elif(Timeupdate.minute==0 or Timeupdate.minute==30):
        try:
            api.update_status(status=df_has)
            print('Descibe')
            time.sleep(60)
        except:
            msg='Hastag data Error  '+str(Time)
            r = requests.post(url, headers=headers , data = {'message':msg})
            time.sleep(60)
            
    elif(Timeupdate.hour==20 and Timeupdate.minute==10):
        SCREEN_NAME='KumaginTrend'
        followers = api.followers_ids(SCREEN_NAME)
        friends = api.friends_ids(SCREEN_NAME)
        for f in friends:
            if f not in followers:       
                api.destroy_friendship(f)
        for f in followers:
            if f not in friends:       
                api.create_friendship(f)
    elif(Timeupdate.hour==20 and Timeupdate.minute==40):
        qqq=[]

        

    time.sleep(30)
    print(Timeupdate.minute)




