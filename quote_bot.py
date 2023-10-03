import tweepy
import random
import schedule
import time
from config import consumer_key, consumer_secret, access_token, access_token_secret

# Authenticate to Twitter
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Read quotes from quotes.txt into a list
with open('quotes.txt', 'r') as file:
    quotes = file.read().splitlines()

# Function to tweet a random quote
def tweet_quote():
    quote = random.choice(quotes)
    # Post Tweet
    client.create_tweet(text=quote)

# Schedule a daily tweet at 12:00 PM
schedule.every().day.at("12:00").do(tweet_quote)

while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep for a second to avoid excessive CPU usage

