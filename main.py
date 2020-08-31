import tweepy
from tweepy import OAuthHandler
from tweepy import API
import datetime as dt
import  time
from os import environ
import json

import pandas as pd

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
        if 'ASDFGHJ' not in i["name"]:
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
        #print('Maximum')
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
    #print('dfcom')
    return(df,now)


listhas=[]


while True:
    Timeupdate=dt.datetime.now()
    if(Timeupdate.minute==0 or Timeupdate.minute==30):
        Time=str(Timeupdate.strftime("%x"))+'  '+str(Timeupdate.strftime("%X"))
        trend_text=trend_twitter()
        text1=top10(trend_text[0],0,5)
        api.update_status(status=text1)
        text2=top10(trend_text[0],5,10)
        time.sleep(40)
        api.update_status(status=text2)
        
        Hashtag=top10(trend_text[0],0,10)
        for i in Hashtag:
            if i not in listhas:
                hashtag=i
                listhas.append(i)
                break
        Retweets=" -filter:retweets"   #  " -filter:retweets"  ไม่รวม Retweet  , ""  รวม Retweet
        lang='' #'th' , 'en' , 'jp'  เว้นว่างสำหรับทุกภาษา 
        df,now=twitter_data(hashtag,lang,Retweets) 
        text_has=hashtag+' のデータ'+'   '+str(now)+'\nツイート   :  '+str(len(df))+'\nアカウント  :  '+str(df[['ids']].drop_duplicates().count()[0])+'\nリツイート  :  '+str(df['Retweet'].sum(axis = 0, skipna = True))+'\nいいねの数  :  '+str(df['Favorite'].sum(axis = 0, skipna = True))+'\n関連ハッシュタグ・トップ3'
        df_has=related_hashtag(df,text_has)
        time.sleep(60)
                
    if(Timeupdate.minute==15 or Timeupdate.minute==45):
        try:
            api.update_status(status=df_has)
            time.sleep(60)
            if(len(listhas)>10):
                listhas.pop(0)
        except:
            time.sleep(60)        
        
        
        
        
        
        
        
        
    time.sleep(40)



