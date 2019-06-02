import tweepy
from tweepy import OAuthHandler
import datetime
from operator import itemgetter

import twitter_credentials

def get_most_retweetted(hashtag):
	auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
	auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth,wait_on_rate_limit=True)

	now = datetime.datetime.now()
	date = str(now.year) + '-' + str(now.month) + '-' + str(now.day)

	list_tweets = []

	for tweet in tweepy.Cursor(api.search,q=hashtag, lang="en", since=date).items(20):
		tweet_obj = (tweet.id, tweet.text, tweet.retweet_count)
		list_tweets.append(tweet_obj)
		# print(str(tweet_obj) + "\n")
	
	return max(list_tweets, key = itemgetter(2))


if __name__ == "__main__":
	# Ask the hashtag the user is interested in
	hashtag = input("Hashtag: ")
	print(get_most_retweetted(hashtag))
