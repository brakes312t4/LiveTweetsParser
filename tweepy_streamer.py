from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials

# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
	"""
	Class for streaming and processing live tweets.
	"""
	def __init__(self):
		pass

	def stream_tweets(self, fetched_tweets_filename, hash_tag_list, lang_list=["en"]): # Default english
		# This handles Twitter authentification and the connection to Twitter Streaming API
		listener = StdOutListener(fetched_tweets_filename)
		auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
		auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
		stream = Stream(auth, listener)

		# This line filters Twitter Streams to capture data by the keywords
		stream.filter(track=hash_tag_list, languages=lang_list)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
	"""
	This is a basic listener that just prints received tweets to stdout.
	"""
	def __init__(self, fetched_tweets_filename):
		self.fetched_tweets_filename = fetched_tweets_filename

	def on_data(self, data):
		try:
			print(data)
			with open(self.fetched_tweets_filename, 'a') as tf: # Append to file
				tf.write(data)
			return True
		except BaseException as e:
			print("Error on_data %s" % str(e))
		return True

	def on_error(self, status):
		print(status)


if __name__ == "__main__":
	# Authenticate and connect to Twitter Streaming API.
	hash_tag_list = ["#NikiLauda"] # Put here the list of hashtags or keywords
	lang_list = ["en"]
	fetched_tweets_filename = "tweets.json" # Type here the filename

	twitter_streamer = TwitterStreamer()
	twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list, lang_list)
