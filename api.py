# TWEEPY API FILE
# Margaret Gorguissian
# 8/20/2017

import tweepy
from twitter_keys import get_keys

def get_API():
    access_token, access_secret, consumer_token, consumer_secret = get_keys()
    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    return api
