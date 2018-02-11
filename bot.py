# thanks to @ejmg for the template

from secret import ACCESS_SECRET, ACCESS_TOKEN, CONSUMER_KEY, CONSUMER_SECRET
import tweepy as ty
import random as r
import datetime as t
import time

def setTwitterAuth():
    auth = ty.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = ty.API(auth)
    return api

def testTweet(api):
    api.update_status("test tweet #{}"
                      .format(r.randint(0, 10000)))

def tweetLyric(api, hr, lines):
    while(hr == t.datetime.now().second):
        time.sleep(10)
    hr = t.datetime.now().second
    api.update_status(randLine(lines))
    print(hr)
    tweetLyric(api, hr, lines)

def randLine(lines):
    line = r.choice(lines)
    line = line.replace("+", "\n")
    print(line)
    return line

if __name__ == "__main__":
    api = setTwitterAuth()
    user = api.me()
    print(user.screen_name)
    print("bot started...")

    hr = t.datetime.now().second
    print(hr)

    lines = open('tweets.txt', 'r').read().splitlines()
    api.update_status(randLine(lines))
    tweetLyric(api, hr, lines)
