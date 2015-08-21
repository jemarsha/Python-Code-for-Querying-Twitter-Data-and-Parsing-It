#!/usr/bin/env python

from slistener import SListener
import time, tweepy, sys

## auth. 

## Eventually you'll need to use OAuth. Here's the code for it here.
## You can learn more about OAuth here: https://dev.twitter.com/docs/auth/oauth
consumer_key        = 'XV3PjLpgl3DaUgDOlCBoA'
consumer_secret     = 'CNdclE7WDzzKzjlo2nEARsQ8tlmmGsl9aNsY8q7Z5A'
access_token        = '1514350788-hio1Ugbrnsi9sxClNfNTNroXCNnwghNpDAbMCHX'
access_token_secret = 'bFQsbRGoCLet1iioOaUHz11bLs0kohZbrjlQvBoaZE0'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def main( mode = 1 ):

#    tweets = api.user_timeline(screen_name = 'DrKeithBush')
    tweets = api.user_timeline(user_id = 42989008)

    for tweet in tweets:
        print(tweet.text)

if __name__ == '__main__':
    main()

