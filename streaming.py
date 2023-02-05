"""
Created on Wed Mar 10 11:00:54 2021

@author: Simon Groß, LucidProgramming on Youtube, github.com/twitterdev/Twitter-API-v2-sample-code

This code provides the possibility to get Twitter data through different methods.
The GetTweetsScweet Class can be used without any API access, but in poses many limitations.

The Classes with 'Tweepy' at the beginning use the Tweepy-library and are based on
LucidProgrammings' Youtube Series on the Twitter API (https://www.youtube.com/watch?v=wlnx-7cm4Gg), however were modified
to fit this use-case
The require only a normal developer-account which can be easily obtained after an application on
https://developer.twitter.com/en
"""

################ Other Modules ################

import time
import json
import pickle
import pandas as pd
import tweepy as tw
from tweepy.streaming import StreamListener

#bt = os.environ.get('BEARER_TOKEN')

bt = ""
consumer_key = 'F08q1o4skqkiR0nuR2YnILSob'
consumer_secret = 'HHjitrVhnmQ3BViLsIVZpGKQfzJo45jAbBnVEaGq2Ra14Rmo8E'

access_token = "1237766974589014022-z5qD33nrfRmDV5FPdrquHtE1uouMqB"
access_token_secret = "Rcv41dBaU1ipImj0nXjHjwvJNatnGdaD5Jhq9KOawcRUK"

class TweepyTwitterClient():
    def __init__(self, twitter_user=None):
        """
        Parameters
        ----------
        twitter_user : string, optional
            the User on whom the functions are performed on. 
            The default is the user whom the consumer_key is registered to.
        """
        self.auth = TweepyTwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = tw.API(self.auth)
        self.twitter_user = twitter_user
        
    def get_twitter_client_api(self):
        return self.twitter_client
        
    def get_tweets_user_timeline_tweets(self, num_tweets):
        """
        Get the timeline of the user
        Parameters
        ----------
        num_tweets: number of timeline tweets
        """
        tweets = []
        for tweet in tw.Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets
    
    def get_friend_list(self, num_friends):
        friend_list = []
        for friend in tw.Cursor(self.twitter_client.friends, id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list
    
class TweepyTwitterAuthenticator():
    def __init__(self):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        
    def authenticate_twitter_app(self, login_private=True):
        """
        Parameters
        ----------
        login_private : bool, optional
            Do you need access to your personal Twitter account? The default is False.

        Returns
        -------
        auth : TYPE
            the authenticator object.
        """
        auth = tw.OAuthHandler(self.consumer_key, self.consumer_secret)#, self.access_token, self.access_token_secret)
        if login_private:
            auth.set_access_token(access_token, access_token_secret)
        return auth

class TweepyTwitterStreamer():
    '''
    Streaming & Processing live Tweets
    '''
    def __init__(self, time_limit=5):
        self.time_limit = time_limit
        self.twitter_authenticator = TweepyTwitterAuthenticator()
        

        
    def stream_tweets(self, hashtag_list, filter=True):

        listener = TweepyTwitterListener(time_limit=self.time_limit)
        
        auth = self.twitter_authenticator.authenticate_twitter_app()
        
        
        stream = tw.Stream(auth, listener)

        if filter:
            stream.filter(track=hashtag_list)
            
        else:
            stream.filter(locations=[-180,-90,180,90])
        
        tweets = listener.tweets
        return tweets

class TweepyTwitterListener(StreamListener):
    '''
    Prints Tweets to stdout
    '''
    # def __init__(self, fetched_tweets_filename):
    #     self.fetched_tweets_filename = fetched_tweets_filename

    def __init__(self, time_limit=2):
        self.start_time = time.time()
        self.limit = time_limit
        self.tweets = []

    
    def on_data(self, data):
        if (time.time() - self.start_time) < self.limit:
            # self.saveFile.write(data)
            # self.saveFile.write('\n')

            self.tweets.append(json.loads(data))
            return True
        else:
            self.tweets.append(json.loads(data))
            return False
    
    def on_error(self, status):
        if status == 420:
            # Return False in case of rates limit
            print(status)
            return False
        print(status)