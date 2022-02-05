import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from emoji import demojize
from statistics import mean

# source: https://predictivehacks.com/how-to-run-sentiment-analysis-in-python-using-vader/

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
        self.cleanMessage = 0

    """
    formats the message
    """
    def cleanMsg(self, msg):
        msg = demojize(msg)
        message = msg.split(' ')[1:]
        return message
    """
    gets a message and adds it to the buffer.
    it also updates the overall sentiment 
    """
    def recieve(self, msg):
        if self.cleanMessage:
            msg = self.cleanMsg(msg)
        print(msg)
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
    def normalize(self, value) -> float:
        value += 1
        value /= 2
        return value

    def getSentiment(self) -> float:
        return self.normalize(self.sentiment)
    
    def setNumComments(self, num):
        self.numComments = num

    def getNumComments(self) -> int:
        return self.numComments

analyzer = Analyzer()
strings = ["i fucking hate this stream", "omg this is so funny", 
"hahahaha", "sadge :(", "please respond", "how's the weather today?"]

for string in strings:
    analyzer.recieve(string)
    print(analyzer.getSentiment())
    print("\n")



"""
to run:
pip install vaderSentiment
pip install nltk
"""


