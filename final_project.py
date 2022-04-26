# -*- coding: utf-8 -*-
"""

Original file is located at
    https://colab.research.google.com/drive/1YJfoqIE4uLvoaiXsaKgUMtYfTwDvAsAI
"""

#imports the basic libraries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

from google.colab import files 
uploaded = files.upload()

#reads the csv file
log = pd.read_csv('clothing.csv')
log.head()

log.shape

!pip install textblob

import nltk
nltk.download('stopwords')
from textblob import TextBlob
from nltk.corpus import stopwords
from textblob import Word


#replaces the null values in the review column
log = log[log['Review Text'].notnull()]

#converts all words to lowercase
log['Review Text'] = log['Review Text'].apply(lambda x: " ".join(x.lower() for x in x.split()))

#removes the punctuation
log['Review Text'] = log['Review Text'].str.replace('[^\w\s]', "")

#removing the stopwords
stop = stopwords.words('english')
log['Review Text'] = log['Review Text'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))

#correcting the spelling 
log['Review Text'] = log['Review Text'].apply(lambda x: str(TextBlob(x).correct()))

#lemmatization to break each word down the root and group similar ones
log['Review Text'] = log['Review Text'].apply(lambda x: str(TextBlob(x).correct()))

from wordcloud import WordCloud
from wordcloud import STOPWORDS

#created a new data frame to look at the text in the reviews
reviews = log 
reviews.dropna(inplace = True)

#creates objects that store each possible rating 
rating_1 = reviews[reviews['Rating'] == 1]
rating_2 = reviews[reviews['Rating'] == 2]
rating_3 = reviews[reviews['Rating'] == 3]
rating_4 = reviews[reviews['Rating'] == 4]
rating_5 = reviews[reviews['Rating'] == 5]

#concatenates all the series/summaries for each ratig into one data frame
reviews_sample = pd.concat([rating_1, rating_2, rating_3, rating_4, rating_5], axis = 0)
reviews_sample.reset_index(drop=True, inplace=True)

#converts the series into string representation to create the wordcloud 
reviews_str = reviews_sample.to_string()
wordcloud = WordCloud(background_color='white').generate(reviews_str)
plt.figure(figsize = (10,10))
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")
plt.show()

#creates individal series for the positive and negative reviews based on their ratings
negative_reviews = reviews_sample[reviews_sample['Rating'].isin([1,2])]
positive_reviews = reviews_sample[reviews_sample['Rating'].isin([4,5])]

#converts each series to string representation
negative_reviews_str = negative_reviews.to_string()
positive_reviews_str = positive_reviews.to_string()

#process of creating the wordcloud for 'negative' words
wordcloud_negative = WordCloud(background_color ='white').generate(negative_reviews_str)
wordcloud_positive = WordCloud(background_color = 'white').generate(positive_reviews_str)
fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(211)
ax1.imshow(wordcloud_negative, interpolation = 'bilinear')
ax1.axis("off")
ax1.set_title("Reviews with Negative Ratings")

#process of creating the wordcloud for 'positive' words
fig = plt.figure(figsize=(10, 10))
ax2 = fig.add_subplot(212)
ax2.imshow(wordcloud_negative, interpolation = 'bilinear')
ax2.axis("off")
ax2.set_title("Reviews with Positive Ratings")

!pip install vaderSentiment

#importing the modules and libraries needed to work in conjunction with vaderSentiment
import seaborn as sns
import re
import os
import sys 
import ast

plt.style.use('fivethirtyeight')
cp = sns.color_palette()

#downloads the vader tool and imports the sentimen intensity analyzer
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

#generate the sentiments for every sentence in the csv file
emptyline = []
for row in log['Review Text']:
  vs = sid.polarity_scores(row)
  emptyline.append(vs)

#create new dataframe that has the sentiments
log_sentiments=pd.DataFrame(emptyline)
log_sentiments.head()

log_new = pd.concat([log.reset_index(drop = True), log_sentiments], axis=1)
log_new.head(3)

#creates dataframe with binary sentiment analysis based on compound sum
log_new['Sentiment'] = np.where(log_new['compound'] >=0, 'Positive', 'Negative')
log_new.head(5)

#creates a nar graph with the sentiment count
result = log_new['Sentiment'].value_counts()
result.plot(kind='bar', rot=0, color=['red', 'blue']);
