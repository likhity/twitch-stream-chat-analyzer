# source: https://predictivehacks.com/how-to-run-sentiment-analysis-in-python-using-vader/
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from emoji import demojize
import numpy as np
from statistics import mean


''' It returns 1/(1+exp(-x)). where the values lies between zero and one '''
def sigmoid(x):
    return 1/(1+np.exp(-x))


"""
    A class that stores the previous x messages from Twitch chat
    and continually updates the mean sentiment
"""
class Analyzer:
    def __init__(self):
        self.buff = []
        # nltk.download('vader_lexicon')
        self.analyzer = SentimentIntensityAnalyzer()
        #initialize neutral sentiment - Ranges from -1 to 1
        self.sentiment = 0.0
        self.numComments = 10
        self.cleanMessage = 1

    """
    formats the message
    """
    def cleanMsg(self, msg):
        msg = demojize(msg)
        message = msg.split(' ')[1:]
        return ' '.join(message)
    """
    gets a message and adds it to the buffer.
    it also updates the overall sentiment 
    """
    def recieve(self, msg):
        if self.cleanMessage:
            msg = self.cleanMsg(msg)
        print(msg) #comment this if you don't want verbose output
        scores = self.analyzer.polarity_scores(msg)
        # an overall score that combines pos, neg, and neutral
        score = float(scores['compound'])
        #remove the first element of the buffer if it overflows
        if len(self.buff) > self.numComments:
            del self.buff[0]
        self.buff.append(score)
        self.sentiment = mean(self.buff)

    """
    takes in a float between -1 and 1 and returns a float from 0 to 1
    """
    def normalize(self, value) -> int:
        # makes the values wider ranging
        value *= 6
        # this returns a value from 0 to 1
        value = sigmoid(value)
        rounded = int(value*100+ 0.5)
        if rounded > 100:
            rounded = 99
        # now range is 0 to 100
        return rounded

    def getSentiment(self) -> int:
        var = self.normalize(self.sentiment)
        print(var)
        return var

    def setNumComments(self, num):
        self.numComments = num

    def getNumComments(self) -> int:
        return self.numComments
