import tweepy
from tweepy import OAuthHandler
import json

import twitter_credentials

# Ask the hashtag the user is interested in and the filename
hashtag = input("Hashtag: ")
filename = input("Output filename: ")

auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)

for tweet in tweepy.Cursor(api.search,q=hashtag, lang="en", since="2019-05-29").items(100):
	tweet_python_dictionary = {
		"id":  tweet.id,
		"created_at": str(tweet.created_at),
		"text": tweet.text,
		"user" : {
			"id" : tweet.user.id,
			"name" : tweet.user.name, # name of the user, e.g. "Wei Xu"
			"screen_name" : tweet.user.screen_name # name of the user account, e.g. "cocoweixu"
		},
		"retweet_count": tweet.retweet_count
	}
	
	# Convert the dictionary into a JSON object and print it
	tweet_json_object = json.dumps(tweet_python_dictionary)	

	with open(filename, "a") as tf:
		tf.write(str(tweet_json_object) + "\n")
		print(str(tweet_json_object) + "\n")
