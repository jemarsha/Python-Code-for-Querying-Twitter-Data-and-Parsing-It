#!/usr/bin/env python

from scipy.stats import linregress
import numpy as np
import matplotlib.pyplot as plt

from slistener import SListener
import time, tweepy, sys

import random

import itertools

## auth. 

## Eventually you'll need to use OAuth. Here's the code for it here.
## You can learn more about OAuth here: https://dev.twitter.com/docs/auth/oauth
consumer_key        = 'XV3PjLpgl3DaUgDOlCBoA'
consumer_secret     = 'CNdclE7WDzzKzjlo2nEARsQ8tlmmGsl9aNsY8q7Z5A'
access_token        = '1514350788-hio1Ugbrnsi9sxClNfNTNroXCNnwghNpDAbMCHX'
access_token_secret = 'bFQsbRGoCLet1iioOaUHz11bLs0kohZbrjlQvBoaZE0'

#----------------------------------------
#----------------------------------------
#----------------------------------------

def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

def getTwitterAccountIdsFromFile(file):
    ids = []
    with open(file,'r') as fin:
        for id in nonblank_lines(fin):
            id.strip()
            ids.append(id)

    return(ids)


def getTwitterAccountIds(gameClass, wordType):

    gameNames = './'+gameClass+'_names.txt'
    gamePath = './'+gameClass+'/'

    # Build an array of games
    names = [line.strip() for line in open(gameNames)]

    nv_ids = []
    v_ids = []
    
    for name in names:

        nv_ids.append(getTwitterAccountIdsFromFile(gamePath+name+wordType+'_nv'))
        v_ids.append(getTwitterAccountIdsFromFile(gamePath+name+wordType+'_v'))
        
    return(v_ids,nv_ids)

def convertListFormat(ids_v):
    ids_v2 = list(itertools.chain.from_iterable(ids_v))
    ids_v_num = []
    for item in ids_v2:
        ids_v_num.append(int(item))
    return(ids_v_num)

def getTweets(gameClass,  wordType, N):
    
    ids_v, ids_nv = getTwitterAccountIds(gameClass,wordType)  

    #Reformat Twitter Ids
    ids_v = convertListFormat(ids_v)
    ids_nv = convertListFormat(ids_nv)

    ##Select N random pairs of v and nv ids for analysis
    rand_indices = random.sample(range(len(ids_v)), N)
    rand_ids_v = []
    rand_ids_nv = []
    for r in rand_indices:        
        rand_ids_v.append(ids_v[r])
        rand_ids_nv.append(ids_nv[r])
        print(str(ids_v[r])+", "+str(ids_nv[r]))

    #Formate tweet lists
    tweets_v = []    
    out_ids_v = []
    tweets_nv = []
    out_ids_nv = []
    
    #Capture Word-Users' Tweets
    for id in rand_ids_v:
        print(id)
        tweet_list = api.user_timeline(user_id = id)
        for raw_tweet in tweet_list:
            tweets_v.append(raw_tweet.text.encode('utf-8'))
            out_ids_v.append(id)
            
    #Capture Random Users' Tweets
    for id in rand_ids_nv:
        print(id)
        tweet_list = api.user_timeline(user_id = id)
        for raw_tweet in tweet_list:
            tweets_nv.append(raw_tweet.text.encode('utf-8'))
            out_ids_nv.append(id)
            
    return(tweets_v, out_ids_v, tweets_nv, out_ids_nv)

#----------------------------------------
#----------------------------------------
#----------------------------------------

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Define Search
gameClass = 'Everyone'  #Everyone, Teen, Mature
wordType = 'Violent'    #Violent, Sexual
N = 2   
ext = random.randint(0,1000000)

#Capture Ids
tweets_v, ids_v, tweets_nv, ids_nv = getTweets(gameClass,wordType, N)

print(tweets_v)
print(tweets_nv)

v_outputfile = gameClass+wordType+'_v_tweets_'+str(ext)
nv_outputfile = gameClass+wordType+'_nv_tweets_'+str(ext)

ids_v_outputfile = gameClass+wordType+'_ids_v_tweets_'+str(ext)
ids_nv_outputfile = gameClass+wordType+'_ids_nv_tweets_'+str(ext)

with open(v_outputfile,'w') as fout:
    for tweet in tweets_v:
        fout.write(tweet + "\n")

with open(nv_outputfile,'w') as fout:
    for tweet in tweets_nv:
        fout.write(tweet + "\n")

with open(ids_v_outputfile,'w') as fout:
    for id in ids_v:
        fout.write(str(id) + "\n")

with open(ids_nv_outputfile,'w') as fout:
    for id in ids_nv:
        fout.write(str(id) + "\n")

