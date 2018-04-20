#!usr/bin/python

## Shane Ryan

import json
import re
from textblob import TextBlob

## read tweets in from source file in easily accessible object format
class Tweet(object):
    tweet_id = 0
    text = ""
    hashtags = list()
    retweets = 0
    user_id = 0
    time = ""
    sentiment = 0

    def __init__(self, tweet_id, text, hashtags, retweets, user_id, time):
        self.tweet_id = tweet_id
        self.text = text
        self.hashtags = hashtags
        self.retweets = retweets
        self.user_id = user_id
        self.time = time
        self.sentiment = self.get_tweet_sentiment()

    def get_tweet_sentiment(self):
        analysis = TextBlob(self.text)
        # sentiment
        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1


def process_tweet(raw_tweet):
    clean_text = ' '.join(re.sub("""(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) \\
        |(\w+:\/\/\S+)""", " ", raw_tweet['text']).split())
    tweet = Tweet(raw_tweet['id'], clean_text, raw_tweet['hashtags'],
            raw_tweet['retweets'], raw_tweet['user_id'], raw_tweet['time'])
    return tweet

def import_tweets(filename):
    raw_tweets = list()
    with open(filename) as source:
        for line in source:
            raw_tweets.append(json.loads(line))

    return raw_tweets

raw_tweets = import_tweets('demo.appa.out.txt')

tweet_data = list()
for tweet in raw_tweets:
    tweet_data.append(process_tweet(tweet))

sentiment_block_score = 0
retweet_block_score = 0
for n, tweet in enumerate(tweet_data):
    sentiment_block_score += tweet.sentiment
    retweet_block_score += tweet.retweets
    print("""Tweet %d\n\nContent:\n%s\n\nSentiment:\t%d\n\nTime:\t%s\n\n"""
            % (n+1, tweet.text, tweet.sentiment, tweet.time))

print("Total sentiment score for block: %d" % sentiment_block_score)
print("Weighted by retweets: %d" % retweet_block_score)




