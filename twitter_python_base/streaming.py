#!/usr/bin/env python

from slistener import SListener
import time, tweepy, sys

## Eventually you'll need to use OAuth. Here's the code for it here.
## You can learn more about OAuth here: https://dev.twitter.com/docs/auth/oauth
#consumer_key        = ""
#consumer_secret     = ""
#access_token        = ""
#access_token_secret = ""
access_token =  '269886955-wwhbqVVZ5YfZ6eCpWrG7V0IDYYZkn5nc28BvOOeB'
access_token_secret = 'mlcmb8PPmsG8k7PWIMU6xLPHkhoOl9a9AixUcCUhE'
consumer_key = 'VzG8pcmNLclguAIKhN0ihQ'
consumer_secret = 'NVwmZnJNoHTG72HSEEdhVJ0wpabIqJnzYOEZ8ZhMq1o'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def main( mode = 1 ):

    track  = ['sochi']
    follow = []
            
    listen = SListener(api, 'test')

    stream = tweepy.Stream(auth, listen)

    print "Streaming started on %s users and %s keywords..." % (len(track), len(follow))

    try: 
        stream.filter(track = track, follow = follow)
        #stream.sample()
    except:
        print "error!"
        stream.disconnect()

if __name__ == '__main__':
    main()

