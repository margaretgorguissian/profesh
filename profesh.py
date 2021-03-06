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
LINKS = []
SWEAR_WORDS = re.compile('fuck|bitch|shit|cunt|dick|pussy')
# Here are just some "unprofessional" twitters I frequequent retweet from. Gonna come up with a cleaner way to do this later.
FORBIDDEN_USERS = ["ClickHole", "Reductress", "iamcardib", "GlowNetflix", "Raquel_Savage", "claudiachoxo", "HAUTEVIOLENCE"]
API = get_API()

def process_tweets():
    recent_tweets = API.user_timeline(TWITTER_NAME, count = 8, include_rts = True)
    for tweet in recent_tweets:
        post = professional_tweet(tweet)
        try:
            if post.entities['urls']:
                 if hasattr(post, 'retweeted_status'):
                      API.retweet(post.id)
                      print("Tweet retweeted")
                 else:
                      for url in post.entities['urls']:
                          LINKS.append(url['expand_url'])
        except AttributeError:
             print("Tweet does not contain link.")

def professional_tweet(tweet):
    # check tweet source
    try:
        if tweet.retweeted_status.user.screen_name in FORBIDDEN_USERS:
            return None
    except AttributeError:
        if SWEAR_WORDS.search(tweet.text):
           return None
    try: 
       return not tweet.possibly_sensitive
    except AttributeError:
       return tweet

def post_list:
    print LINKS
    LINKS.clear()

def retweet(tweet_id):
    API.retweet(tweet_id)

def post_tweet(text):
    API.update_status(text)

tweet_scheduler = BackgroundScheduler()
# I tweet a lot. Every 20 minutes, go through my tweets and check if there's anything new to retweet
tweet_scheduler.add_job(process_tweets, 'interval', minutes=20, id='process_tweets')
# At midnight, post a list of all links I posted myself, so I can decide what I want to post on my other account.
tweet_scheduler.add_job(post_list, 'cron', hour=00, id='post_list')
