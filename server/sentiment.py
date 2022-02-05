import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import twitter_samples 
from emoji import demojize
import re
from statistics import mean

class Analyzer:
    def __init__(self):
        self.buff = []
        # nltk.download('vader_lexicon')
        self.analyzer = SentimentIntensityAnalyzer()
        #initialize neutral sentiment - Ranges from -1 to 1
        self.sentiment = 0
        self.numComments = 10

    def cleanMsg(self, msg):
        msg = demojize(msg)
        message = msg.split(' ')[1:]
        return message

    def recieve(self, buff):
        msg = self.cleanMsg(buff)
        print(msg)
        scores = self.analyzer.polarity_scores(msg)
        # an overall score that combines pos, neg, and neutral
        score = float(scores['compound'])
        if len(buff) > self.numComments:
            self.buff = []
        self.buff.append(score)
        self.sentiment = mean(self.buff)

    def getSentiment(self):
        return self.sentiment
    
    def setNumComments(self, num):
        self.numComments = num

    def getNumComments(self):
        return self.numComments

analyzer = Analyzer()
strings = ["i fucking hate this stream", "omg this is so funny", 
"hahahaha", "sadge :(", "please respond", "how's the weather today?"]

for string in strings:
    analyzer.recieve(string)
    print(analyzer.getSentiment())
    print("\n")



"""
pip install vaderSentiment
pip install nltk
pip install markdown 
pip install pandas matplotlib tensorflow
"""


# https://predictivehacks.com/how-to-run-sentiment-analysis-in-python-using-vader/