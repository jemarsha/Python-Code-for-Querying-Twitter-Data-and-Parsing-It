
#!/usr/bin/env python

from slistener import SListener
import time,json, tweepy, sys, getopt

## auth. 

## Eventually you'll need to use OAuth. Here's the code for it here.
## You can learn more about OAuth here: https://dev.twitter.com/docs/auth/oauth
##consumer_key        = 'XV3PjLpgl3DaUgDOlCBoA'
##consumer_secret     = 'CNdclE7WDzzKzjlo2nEARsQ8tlmmGsl9aNsY8q7Z5A'
##access_token        = '1514350788-hio1Ugbrnsi9sxClNfNTNroXCNnwghNpDAbMCHX'
##access_token_secret = 'bFQsbRGoCLet1iioOaUHz11bLs0kohZbrjlQvBoaZE0'

# OAuth process, using the keys and tokens
##auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
##auth.set_access_token(access_token, access_token_secret)
##api = tweepy.API(auth)

def main(argv):


## auth.                                                                        

## Eventually you'll need to use OAuth. Here's the code for it here.            
## You can learn more about OAuth here: https://dev.twitter.com/docs/auth/oauth
## Get this from twitter: I left the comments blank to be filled in with your information
    consumer_key        = ''
    consumer_secret     = ''
    access_token        = ''
    access_token_secret = ''

# OAuth process, using the keys and tokens                                      
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)


    name = 'default'
    maxTweets = 35
    track  = [name]
    follow = []

   
    try:
        opts, args = getopt.getopt(argv,"hk:m:",['keyword','maxtweets'])
    except getopt.GetoptError:
        print 'streaming2.py -k  <keyword> -m <maxtweets>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'datacount.py -k <keyword> -m <maxtweets>'
            sys.exit()
        elif opt in ("-k", "--keyword"):
            name = arg
            track = [name]
        elif opt in ("-m", "--maxtweets"):
            maxTweets = arg
    print (name)
    print (maxTweets)
    listen = SListener(api,name,maxTweets)
    stream = tweepy.Stream(auth, listen)

    print "Streaming started on %s users and %s keywords..." % (len(track), len(follow))
    
    try: 
        stream.filter(track = track, follow = follow)
        #stream.sample()
    except:
        stream.disconnect()

if __name__ == '__main__':
    main(sys.argv[1:])

