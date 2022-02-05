import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import twitter_samples 


strings = ["i fucking hate this stream", "omg this is so funny", 
"hahahaha", "sadge : (", "please respond", "how's the weather today?"]

analyzer = SentimentIntensityAnalyzer()



# nltk.download('twitter_samples')
# nltk.download('vader_lexicon')
 
# # get 5000 posivie and negative tweets
# all_positive_tweets = twitter_samples.strings('positive_tweets.json')
# all_negative_tweets = twitter_samples.strings('negative_tweets.json')
 
# analyzer = SentimentIntensityAnalyzer()
# # positive
# print(all_positive_tweets[100])
# analyzer.polarity_scores(all_positive_tweets[100])
# print(all_negative_tweets[20])
# analyzer.polarity_scores(all_negative_tweets[20])
# my_labels = [1]*len(all_positive_tweets)
# negative_labels = [0]*len(all_negative_tweets)
# my_labels.extend(negative_labels)
 
# all_positive_tweets.extend(all_negative_tweets)
 
# df = pd.DataFrame({'tweets' : all_positive_tweets, 
#                    'my_labels' : my_labels})
# df['neg'] = df['tweets'].apply(lambda x:analyzer.polarity_scores(x)['neg'])
# df['neu'] = df['tweets'].apply(lambda x:analyzer.polarity_scores(x)['neu'])
# df['pos'] = df['tweets'].apply(lambda x:analyzer.polarity_scores(x)['pos'])
# df['compound'] = df['tweets'].apply(lambda x:analyzer.polarity_scores(x)['compound'])


# print(df)
# df.groupby('my_labels')['compound'].describe()
# df.boxplot(by='my_labels', column='compound', figsize=(12,8))



"""
pip install vaderSentiment
pip install django-filter
pip install djangorestframework
pip install markdown 
pip install pandas matplotlib tensorflow
"""


# https://predictivehacks.com/how-to-run-sentiment-analysis-in-python-using-vader/