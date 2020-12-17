from __future__ import absolute_import, print_function
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json # library to handle json files.
import pandas as pd
import matplotlib.pyplot as plt
import time


# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key = "H6N8M8aUm86D4gzy0fZuR1rbp"
consumer_secret = "5A8O5HXR8YyGqxl12oXdX5EI8zG4YbNjrBr8SIRgUuwxzeAT7S"
# After the step above, you will be redirected to your app’s page.
# Create an access token under the the "Your access token" section
access_token = "1327419207148036096-KFOuNKkJ3GEn2yBp5IOP0dFtfAqDHr"
access_token_secret = "TrwGR1D1LV7u2yG8rKHo6NBq07RvM4gTlow7gM7em6BI4"


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, time_limit=7200):
        self.start_time = time.time()
        self.limit = time_limit
        self.counter = 0
        super(StdOutListener, self).__init__()

    def on_data(self, data):
        if (time.time() - self.start_time) < self.limit:
            # print(data)
            # if we see data then we add 1 (tweet) to counter.
            self.counter += 1
            return True
        else:
            return False
    
    def on_error(self, status):
        print(status)


if __name__ == "__main__":
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    # monitor Tweets sent from Amsterdam (geo-location). question 5. 
    # stream.filter(locations=[4.61, 52.27, 5.07, 52.50])
    # monitor Tweets related to COVID-19. question 6.
    stream.filter(track=['covid','covid-19','corona','coronavirus','lockdown'])
    # print how many tweets we received depending on which filter we do. (question 5&6)
    print(l.counter)