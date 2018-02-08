from secret import ACCESS_SECRET, ACCESS_TOKEN, CONSUMER_KEY, CONSUMER_SECRET
import tweepy as ty
import random

def setTwitterAuth():
    auth = ty.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = ty.API(auth)
    return api

def tweetHelloWorld(api):
    api.update_status("This is an automated tweet"
                      " using a bot! Hello, World! #{}"
                      .format(random.randint(0, 10000)))

if __name__ == "__main__":
    api = setTwitterAuth()
    tweetHelloWorld(api)
