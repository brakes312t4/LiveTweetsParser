import tweepy
from tweepy import OAuthHandler
import datetime
from operator import itemgetter

import twitter_credentials

def get_most_retweetted(hashtag, top_n: int):
	auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
	auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth,wait_on_rate_limit=True)

	now = datetime.datetime.now()
	date = str(now.year) + '-' + str(now.month) + '-' + str(now.day)

	list_tweets = []

	for tweet in tweepy.Cursor(api.search,q=hashtag, lang="en", since=date).items(20):
		tweet_obj = (tweet.text, tweet.retweet_count)
		if tweet_obj not in list_tweets:
			list_tweets.append(tweet_obj)
			# print(str(tweet_obj) + "\n")

	if not list_tweets:
		return [('None', 'None')]

	list_most_retweetted_tweets = []

	for i in range(min(top_n, len(list_tweets))): # this avoids error on max at next line
		top_tweet = max(list_tweets, key = itemgetter(1))
		list_most_retweetted_tweets.append(top_tweet)
		list_tweets.remove(top_tweet)

	return list_most_retweetted_tweets

if __name__ == "__main__":
	# Ask the hashtag the user is interested in
	hashtag = input("Hashtag: ")
	top_n = int(input("Number of tweets: "))
	print(get_most_retweetted(hashtag, top_n))
