# profesh.py
# Margaret Gorguissian
# 8/17/2017

from apscheduler.schedulers.background import BackgroundScheduler
from os import system
from time import sleep
from datetime import datetime
import re

from api import get_API

TWITTER_NAME = "arshile_gorky" #place the twitter handle you would like to take tweets from here
TWEET_WINDOW = True
FOLLOWERS = []
SWEAR_WORDS = re.compile('fuck|bitch|shit|cunt')
# Here are just some "unprofessional" twitters I frequequent retweet from. Gonna come up with a cleaner way to do this later.
FORBIDDEN_USERS = ["ClickHole", "Reductress", "iamcardib", "GlowNetflix", "Raquel_Savage", "claudiachoxo", "HAUTEVIOLENCE"]
API = get_API()

def processTweets():
    recent_tweets = API.user_timeline(TWITTER_NAME, count = 8, include_rts = True)
    links = []
    for tweet in recent_tweets:
        professional_tweet(tweet)
#        try:
#            if tweet.entities['urls']:
#                 if hasattr(tweet, 'retweeted_status'):
#                      API.retweet(tweet.id)
#                      print("Tweet retweeted")
#                 else:
#                      for url in tweet.entities['urls']:
#                          links.append(url['expand_url'])
#        except AttributeError:
#             print("Tweet does not contain link.")

def professional_tweet(tweet):
    if SWEAR_WORDS.search(tweet.text):
         return False   
    # check tweet source
    try:
        if tweet.retweeted_status.user.screen_name in FORBIDDEN_USERS:
            return False
    except AttributeError:
        pass
    try: 
       return not tweet.possibly_sensitive
    except AttributeError:
       return True
    # possibly sensitive is a boolean, so this is my last check
    #return tweet.possibly_sensitive 

processTweets() 
