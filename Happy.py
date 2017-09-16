# Dependencies
import tweepy
import time
import json
import random

# Twitter API Credentials
consumer_key = "CFpLL0ekDU87TUQMyNIL4sWWp"
consumer_secret = "EbZsFaejwDKHQ4PLdrrnG5Qe4cbgtJ119jfT7nQHRpFgqEDZN4"
access_token = "108089777-HGwF61xW9LDDdcj7YKF3R34BfvR3eaRll5LKBMel"
access_token_secret = "IdqcpGygQkygvXqNE4O3XCo69WsrBUUBDixs0VGq5ATOm"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Quotes to Tweet
happy_quotes = [
    "For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
    "Folks are usually about as happy as they make their minds up to be. - Abraham Lincoln",
    "Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi",
    "Count your age by friends, not years. Count your life by smiles, not tears. - John Lennon",
    "Happiness is a warm puppy. - Charles M. Schulz",
    "The happiness of your life depends upon the quality of your thoughts. - Marcus Aurelius",
    "Now and then it's good to pause in our pursuit of happiness and just be happy. - Guillaume Apollinaire"]

# Create function for tweeting
def tweety_happy(tweet):
    
    api.update_status(tweet)

# Twitter credentials

# Tweet a random quote

rand_tweet = happy_quotes[random.randrange(0, len(happy_quotes)-1)]

while(True):
    try:
        tweety_happy(rand_tweet)
    
# Print success message
        print('Success')

    except:
        print('Dup')
# Set timer to run every minute
    time.sleep(60)