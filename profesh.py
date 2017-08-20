# profesh.py
# Margaret Gorguissian
# 8/17/2017

from apscheduler.schedulers.background import BackgroundScheduler
from os import system
from time import sleep
from datetime import datetime

from api import get_API

TWITTER_NAME = "" #place the twitter handle you would like to take tweets from here
TWEET_WINDOW = True
FOLLOWERS = []

def processTweets():
    recent_tweets = API.user_timeline([TWITTER_NAME], [since_id], [max_id], [count], [page])
    for tweet in recent_tweets:
        if not tweet.retweeted and not 
