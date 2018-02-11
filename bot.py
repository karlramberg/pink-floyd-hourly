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
    while(hr == t.datetime.now().hour):
        time.sleep(10)
    hr = t.datetime.now().hour
    api.update_status(randLine(lines))
    print("[x] Tweet successful")
    print("")
    tweetLyric(api, hr, lines)

def randLine(lines):
    line = r.choice(lines)
    print("[x] Tweeting... " + line)
    line = line.replace("+", "\n")
    return line

if __name__ == "__main__":
    print("[x] Bot started")

    api = setTwitterAuth()
    user = api.me()
    print("[x] Authenticated @" + user.screen_name)

    hr = t.datetime.now().hour
    print("[x] Current time - " + str(t.datetime.now()))

    lines = open('tweets.txt', 'r').read().splitlines()
    print("[x] Lyrics loaded")
    print("")

    tweetLyric(api, hr, lines)
