# bot.py

import tweepy
from config import consumer_key, consumer_secret, access_token, access_token_secret

# Set up Twitter API authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

