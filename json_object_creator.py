# Import the necessary package to process data in JSON format
try:
	import json
except ImportError:
	import simplejson as json

import sys

# The input file is read from stdin
if len(sys.argv) < 2:
	sys.exit()

tweets_filename = sys.argv[1]
tweets_file = open(tweets_filename, "r")

for line in tweets_file:
	try:
		# Read one line of the file, convert it into a json object 
		tweet = json.loads(line.strip())
		if 'text' in tweet: # only a message containing 'text' field is a tweet
			# Create a python dictionary
			tweet_python_dictionary = {
				"id":  tweet["id"],
				"created_at": tweet["created_at"],
				"text": tweet["text"],
				"user" : {
					"id" : tweet["user"]["id"],
					"name" : tweet["user"]["name"], # name of the user, e.g. "Wei Xu"
					"screen_name" : tweet["user"]["screen_name"] # name of the user account, e.g. "cocoweixu"
				}
			}
			
			# Convert the dictionary into a JSON object and print it
			tweet_json_object = json.dumps(tweet_python_dictionary)
			print(tweet_json_object)

			print("\n")

	except:
		# read in a line is not in JSON format (sometimes error occured)
		continue
