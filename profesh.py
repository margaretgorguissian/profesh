# profesh.py
# Margaret Gorguissian
# 8/17/2017

from apscheduler.schedulers.background import BackgroundScheduler
from os import system
from time import sleep
from datetime import datetime

from api import get_API

TWITTER_NAME = "arshile_gorky" #place the twitter handle you would like to take tweets from here
TWEET_WINDOW = True
FOLLOWERS = []
SWEAR_WORDS = ["fuck", "bitch", "shit", "cunt", "ass"]
API = get_API()

def processTweets():
    recent_tweets = API.user_timeline(TWITTER_NAME, count = 16, include_rts = True)
    links = []
    for tweet in recent_tweets:
        if hasattr(tweet, 'entities'):
            if tweet.entities['urls']:
                if hasattr(tweet, 'retweeted_status'):
                    API.retweet(tweet.id)
                else: 
                    for url in tweet.entities['urls']:
                        links.append(url['expanded_url'])    

def professional_tweet(tweet):
    #if tweet contains swear words
         #return false
    #if tweet contains bad phrases
         #return false
    #if tweet contains sensitive content
         #return false
    #if tweet contains 
    #return true
processTweets() 
