
# coding: utf-8

# In[2]:

import urllib2
import json
import tweepy
from twitter import *
import requests
import tweepy, time



# In[3]:

ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)


# In[4]:

twitter_stream = TwitterStream(auth = oauth)

search = "textnook"
iterator = twitter_stream.statuses.filter(track = search, language = "en")


# for tweet in iterator:
#     
#     
#     text = tweet["text"]
#     print text
#     
#     

# In[5]:


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)



# In[7]:

tweetlist = ['Lift Off !! ', 'I am alive.', 'I am but a baby now. But I shall grow soon.']

for line in tweetlist: 
    api.update_status(line)
    print line
    print '...'
    time.sleep(15) #15 seconds
    
    


# In[20]:

for tweet in tweepy.Cursor(api.search,q='buy book',geocode='23.3308,79.8143,2100km').items(10):

# Print out usernames of the last 10 people to use #ocean
    print('Tweet by: @' + tweet.user.screen_name)
    print tweet.text


# In[ ]:



