# thanks to @ejmg for the template

from secret import ACCESS_SECRET, ACCESS_TOKEN, CONSUMER_KEY, CONSUMER_SECRET
from collections import deque
import tweepy as ty
import random as r
import datetime as t
import time

def setTwitterAuth():
    auth = ty.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = ty.API(auth)
    return api

def tweetLyric(hr, api, tweets):
    while(hr == t.datetime.now().hour): # wait until a new hour
        time.sleep(10)
    hr = t.datetime.now().hour

    tweet = getTweet(tweets) # get a random tweet

    tweet = tweet.replace("+", "\n") # formatting
    api.update_status(tweet)
    print("[x] Tweet successful")
    print("")

def getTweet(tweets):
    tweet = r.choice(tweets)
    print("[x] Tweeting... " + tweet)
    while(checkHist(tweet) == False): # twitter hates duplicate tweets
        tweet = r.choice(tweets)
        print("[x] Duplicate, Retrying...")
        print("[x] Tweeting... " + tweet)
    return tweet

def checkHist(tweet):
    stati = api.user_timeline(count=96, tweet_mode="extended") # load the past 4 days
    hist = [t.full_text for t in stati]
    for i in hist:
        if tweet == i.replace("\n","+"):
            return False
    return True

if __name__ == "__main__":
    print("[x] Bot started")

    api = setTwitterAuth()
    user = api.me()
    print("[x] Authenticated @" + user.screen_name)

    hr = t.datetime.now().hour
    print("[x] Current time - " + str(t.datetime.now()))

    tweets = open('/opt/pfh/res/tweets.txt', 'r').read().splitlines()
    print("[x] Lyrics loaded")
    print("")

    tweetLyric(hr, api, tweets)