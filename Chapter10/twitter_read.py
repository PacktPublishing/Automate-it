#Read twitter data, categorize it and 
#plot data to generate insight

import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Read tweets
tweets = []
fh = open("twitter_data.txt", "r")
for data in fh:
    try:
        tweets.append(json.loads(data))
    except:
        continue

#Read tweets as pandas data frame
tweet_df = pd.DataFrame()
tweet_df['text'] = map(lambda x: x['text'], tweets)
tweet_df['lang'] = map(lambda x: x['lang'], tweets)

#Group tweets based on language and get the count
tweets_by_lang = tweet_df['lang'].value_counts()

#Plot the data in bar chart
fig, axis = plt.subplots()
sns.set_style("darkgrid")
axis.set_xlabel('Languages', fontsize=15)
axis.set_ylabel('Tweets' , fontsize=15)
clrs = ['green', 'blue', 'red', 'black']
sns_plot = tweets_by_lang[:4].plot(ax=axis, kind='bar', color=clrs)
plt.savefig('language.pdf')
