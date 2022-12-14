#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 00:36:34 2022

@author: Dante
"""
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
 
#reading excel or xlsx files
data = pd.read_excel('articles.xlsx')

#summary of data

data.describe()

#summary of columns
data.info()

#Counting the number of articles per source(publisher)
#format of groupby = df.groupby(['column_to_group'])['column_to_count'].count()

data.groupby(['source_id'])['article_id'].count()

#number of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

#dropping column
data = data.drop('engagement_comment_plugin_count' , axis = 1)

#functions in python

def thisfunction():
    print('this is my first function')

thisfunction()


#creating a keyword flag

keyword = 'crash'

#create a for loop to isolate each title

# lentgh = len(data)
# keyword_flag = []
# for x in range(0,len):
#     heading = data['title'][x]
#     if keyword in heading:
#         flag = 1
#     else:
#         flag = 0
#     keyword_flag.append(flag)

#reating a funciton

def keywordflag(keyword_flag):
    
    length = len(data)
    keyword_flag = []
    for x in range(0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                    flag = 1
            else:
                    flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag

keywordflag = keywordflag('murder')

#creating new cokumn in data dataframe

data['keyword_flag'] = pd.Series(keywordflag)

#SentimentIntensityAnalyzer

sent_int = SentimentIntensityAnalyzer()

text = data['title'][15]
sent = sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

#adding a for loop to extract sentiment per title

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

length = len(data)


for x in range(0,length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)    
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)


data['title_neg_semtiment'] = title_neg_sentiment
data['title_pos_sentiimet'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment



#writing the data

data.to_excel('blogme_clean.xlsx' , sheet_name='blogmedata' , index=False)

















