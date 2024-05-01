import tweepy
from textblob import TextBlob

consumer_key = 'xxxxx'
consumer_secret = 'xxxxx'

acces_token = 'xxxxx'
acces_token_secret = 'xxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acces_token, acces_token_secret)

api = tweepy.API(auth)

public_tweets = api.search_tweets(q='Feminsmo')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
