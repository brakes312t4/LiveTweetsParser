# Import the necessary package to process data in JSON format
try:
	import json
except ImportError:
	import simplejson as json

# We use the file saved
tweets_filename = 'tweets.json'
tweets_file = open(tweets_filename, "r")


for line in tweets_file:
	try:
		# Read in one line of the file, convert it into a json object 
		tweet = json.loads(line.strip())
		if 'text' in tweet: # only a message containing 'text' field is a tweet
			print(tweet['id'])
			print(tweet['created_at'])
			print(tweet['text'])
						
			print(tweet['user']['id'])
			print(tweet['user']['name']) # name of the user, e.g. "Wei Xu"
			print(tweet['user']['screen_name']) # name of the user account, e.g. "cocoweixu"

			print("\n")

	except:
		# read in a line is not in JSON format (sometimes error occured)
		continue
