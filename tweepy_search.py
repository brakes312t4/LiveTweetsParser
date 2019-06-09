import tweepy
from tweepy import OAuthHandler
import datetime
import json

import twitter_credentials

# Ask the hashtag the user is interested in and the filename
hashtag = input("Hashtag: ")
filename = (hashtag.replace("#", "")).replace(" ", "_") + ".json"
# filename = hashtag.replace(" ", "_") + ".json"

auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)

now = datetime.datetime.now()
date = str(now.year) + '-' + str(now.month) + '-' + str(now.day)

list_texts = []

for tweet in tweepy.Cursor(api.search,q=hashtag, lang="en", since=date).items(30):
	if tweet.text not in list_texts:
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

		list_texts.append(tweet.text)

		# Convert the dictionary into a JSON object and print it
		tweet_json_object = json.dumps(tweet_python_dictionary)	

		with open("twitter_datasets/" + filename, "a") as tf:
			tf.write(str(tweet_json_object) + "\n")
			print(str(tweet_json_object) + "\n")
