import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests

#Load the tweets stored in a text file
tweets = []
fh = open("twitter_data.txt", "r")
for data in fh:
    try:
        tweets.append(json.loads(data))
    except:
        continue

#Load the tweets as data frames
probablities = pd.DataFrame()
prob = []

#Go through all the tweets and apply sentiment analysis
for tweet in tweets:
    text = tweet['text']
    r = requests.post(url="http://text-processing.com/api/sentiment/",
		data={"text":text},)
    print r.text	
    if r.status_code == 200:
	ans = json.loads(r.text)
	prob.append(ans["label"])

#Get the setiments and generate counts for each sentiment
probablities['data'] = map(lambda x: x, prob)
p_df = probablities['data'].value_counts()		

#Plot the data using seaborn	
fig, axis = plt.subplots()
sns.set_style("darkgrid")
axis.set_xlabel('Sentiments', fontsize=15)
axis.set_ylabel('Tweets' , fontsize=15)
clrs = ['green', 'yellow', 'red']
sns_plot = p_df.plot(ax=axis, kind='bar', color=clrs)
plt.savefig('sentiments.pdf')
