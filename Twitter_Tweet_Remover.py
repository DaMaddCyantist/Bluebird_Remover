#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Necessary package imports.
# Use pip install python-twitter to import the proper python wrapper


# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_profiling
from twitter import *


# In[ ]:


# Keys and Tokens are created via the Twitter Developer website


# In[ ]:


consumer_key = '***'
consumer_secret = '***'
access_token = '***'
access_secret = '***'


# In[ ]:


# Creates api instance for Twitter


# In[ ]:


api = Api(consumer_key,consumer_secret,access_token,access_secret)


# In[ ]:


# I downloaded my Twitter data from twitter and I am accessing the 'tweet.js' file, which contains all of my tweets


# In[ ]:


the_data = pd.read_json('tweet.js')


# In[ ]:


# Creating a copy of the dataframe and selected only the relevant columns


# In[ ]:


tweets = the_data.copy()
tweets = the_data.loc[:,('id','full_text')]


# In[ ]:


# This step capitilzies all letters in each tweet to account for case sensitivities


# In[ ]:


tweets['full_text'] = tweets.loc[:,['full_text']].apply(lambda x: x.str.upper())


# In[ ]:


# Creates a new dataframe that contains tweets containing the specified word 


# In[ ]:


word = '***'
this_array = []
that_array = []
[this_array.append(x) for x,y in zip(tweets['id'],tweets['new']) if word in y]
[that_array.append(y) for x,y in zip(tweets['id'],tweets['new']) if word in y]
data = {'ID':this_array,'Tweets':that_array}
new_tweets = pd.DataFrame(data)


# In[ ]:


# Subsets most retweets out of dataset and resets the index for proper formatting


# In[ ]:


rule = ~(new_tweets['Tweets'].str.contains('RT'))
final_tweets = new_tweets[rule]
final_tweets.reset_index(drop=True,inplace=True)


# In[ ]:


# Try-Except-Else block to delete each tweet in the final_tweets dataframe.
# Code 144 corresponds to a tweet that is already deleted.
# This also creates an array of ID's that are not able to be deleted due to another error code.


# In[ ]:


error_id_array = []
for ID in final_tweets.ID: 
    try:
        ID = str(ID)
        api.DestroyStatus(ID)
    except TwitterError as e:
        if e.message[0]['code'] == 144:
            print('Tweet Deleted. Skipping...')
        else:
            print('Some other error occured for TweetID: ' + ID)
            error_id_array.append(ID)
    else:
        print('Successfully deleted that Tweet.')


# In[ ]:


consumer_key = 'l6HYjHlvMVRa0D5bohN9emXR9'
consumer_secret = '8re0nFAap9CFOC4lU75YLZNCIdttodrk8Ho7v9Ps5FykmRot2A'
access_token = '1461422742-tbXdpLHGFgfg5Qd6cOysEXbyY8dI8crckvRQqKX'
access_secret = 'EL6OQKAWuXqprmw9rhP4Oz0XBBZSnmF7kvRyrTermWmJL'

