import tweepy
from textblob import TextBlob

consumer_key = 'L7eMpqlvOzU2xu92A3pejtHtu'
consumer_secret = '2frbkDgynEVs2uASmqdDvtaky3WTAd9pbY0rv0nILKfZbfBV1m'

acces_token = '1769519338422239232-V89vSnp9QU8XPjmcM03chIy10wGNvC'
acces_token_secret = 'dmYlaCj0ufhO1F7ChZ4uPXrtdVGXYudwRGyFjC7cvQCqp'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acces_token, acces_token_secret)

api = tweepy.API(auth)

public_tweets = api.search_tweets(q='Feminsmo')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)