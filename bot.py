# Thank you to @ejmg for the template

from secret import ACCESS_SECRET, ACCESS_TOKEN, CONSUMER_KEY, CONSUMER_SECRET
from collections import deque
import tweepy as ty
import random as r

def setTwitterAuth():
    auth = ty.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = ty.API(auth)
    return api

def tweetLyric(api, tweets):

    tweet = getTweet(tweets) # get a random tweet

    tweet = tweet.replace("+", "\n") # formatting
    api.update_status(tweet)
    print("> Tweet successful")
    print("")

def getTweet(tweets):
    tweet = r.choice(tweets)
    print("> Tweeting... " + tweet)
    while(checkHist(tweet) == False): # twitter hates duplicate tweets
        tweet = r.choice(tweets)
        print("> Duplicate, Retrying...")
        print("> Tweeting... " + tweet)
    return tweet

def checkHist(tweet):
    stati = api.user_timeline(count=96, tweet_mode="extended") # load the past 4 days
    hist = [t.full_text for t in stati]
    for i in hist:
        if tweet == i.replace("\n","+"):
            return False
    return True

if __name__ == "__main__":
    print("> Bot started")

    api = setTwitterAuth()
    user = api.me()
    print("> Authenticated @" + user.screen_name)

    tweets = open('/opt/pfh/tweets.txt', 'r').read().splitlines()
    print("> Lyrics loaded")
    print("")

    tweetLyric(api, tweets)
