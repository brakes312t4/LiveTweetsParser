# LiveTweetsParser
Filtering fields of interest from live tweets.
Thanks to [vprusso](https://github.com/vprusso/youtube_tutorials/tree/master/twitter_python/part_1_streaming_tweets) for his useful tutorial on Tweepy.

## Overview
* [twitter_credentials.py](twitter_credentials.py) contains the Twitter credentials.
* [tweepy_streamer.py](tweepy_streamer.py) receives live tweets of a specified hashtag or keyword. Each tweet will be printed on stdout and also stored in a line of a json document.
* [tweepy_streamer_limited.py](tweepy_streamer_limited.py) is a variant that collects a predefined number of tweets at most.
* [tweets_printer.py](tweets_printer.py) reads each line of the previous file and prints id of the tweet, creation time, text, the user's id, name and screen name.
* [json_object_creator.py](json_object_creator.py) reads each line of the streamer output and collects the previous fields in a dictionary. This dictionary is then converted into a JSON object and printed.

It is possible to filter different fields of the Twitter response: just look at [https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object)

## Run it
```json``` and ```simplejson``` are the required Python libraries. Install them globally or in a virtual environment.

```$ python tweepy_streamer.py``` to write the entire tweet objects in the document

```$ python tweets_printer.py <input_filename>.json > <filename>.txt``` to write the filtered fields in a txt file

```$ python json_object_creator.py <input_filename>.json > <filename>.json``` to write every filtered JSON object in a json file 

## Example

That's the JSON response of a single tweet

```{"created_at":"Tue May 21 08:57:54 +0000 2019","id":1130759612280516608,"id_str":"1130759612280516608","text":"RT @LeeMcKenzieTV: I never took for granted any chance to chat with Niki Lauda. When he spoke you listened. A true great, bravery beyond be\u2026","source":"\u003ca href=\"http:\/\/twitter.com\/download\/android\" rel=\"nofollow\"\u003eTwitter for Android\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":845950663595085824,"id_str":"845950663595085824","name":"Elle","screen_name":"Es_Ellie_","location":null,"url":null,"description":"Ballet and BVB09","translator_type":"none","protected":false,"verified":false,"followers_count":21,"friends_count":383,"listed_count":0,"favourites_count":9582,"statuses_count":7984,"created_at":"Sun Mar 26 10:48:50 +0000 2017","utc_offset":null,"time_zone":null,"geo_enabled":false,"lang":"en","contributors_enabled":false,"is_translator":false,"profile_background_color":"000000","profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_tile":false,"profile_link_color":"E81C4F","profile_sidebar_border_color":"000000","profile_sidebar_fill_color":"000000","profile_text_color":"000000","profile_use_background_image":false,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/1036303090071359488\/qb7BfApB_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/1036303090071359488\/qb7BfApB_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/845950663595085824\/1535304958","default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"retweeted_status":{"created_at":"Tue May 21 06:03:04 +0000 2019","id":1130715614992060416,"id_str":"1130715614992060416","text":"I never took for granted any chance to chat with Niki Lauda. When he spoke you listened. A true great, bravery beyo\u2026 https:\/\/t.co\/WrmL4OVLCW","source":"\u003ca href=\"http:\/\/twitter.com\/download\/iphone\" rel=\"nofollow\"\u003eTwitter for iPhone\u003c\/a\u003e","truncated":true,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":21200516,"id_str":"21200516","name":"Lee McKenzie","screen_name":"LeeMcKenzieTV","location":"UK or globetrotting","url":"http:\/\/www.leemckenzie.tv","description":"BBC\/C4 F1, Rugby, Olympics, Paralympics, Wimbledon, Equestrian \ud83d\udc99 travel and natural \ud83c\udf0e http:\/\/Instagram.com\/leemckenzietv FB http:\/\/on.fb.me\/20Ua8MH","translator_type":"none","protected":false,"verified":true,"followers_count":271633,"friends_count":838,"listed_count":5796,"favourites_count":2928,"statuses_count":14601,"created_at":"Wed Feb 18 14:33:09 +0000 2009","utc_offset":null,"time_zone":null,"geo_enabled":false,"lang":"en","contributors_enabled":false,"is_translator":false,"profile_background_color":"000000","profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme4\/bg.gif","profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme4\/bg.gif","profile_background_tile":false,"profile_link_color":"3B94D9","profile_sidebar_border_color":"000000","profile_sidebar_fill_color":"000000","profile_text_color":"000000","profile_use_background_image":false,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/711739929752109057\/YrWgwQ7b_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/711739929752109057\/YrWgwQ7b_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/21200516\/1455724644","default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"is_quote_status":false,"extended_tweet":{"full_text":"I never took for granted any chance to chat with Niki Lauda. When he spoke you listened. A true great, bravery beyond belief and a funny and tough guy. Love to all his family xx #nikilauda","display_text_range":[0,188],"entities":{"hashtags":[{"text":"nikilauda","indices":[178,188]}],"urls":[],"user_mentions":[],"symbols":[]}},"quote_count":3,"reply_count":12,"retweet_count":73,"favorite_count":1310,"entities":{"hashtags":[],"urls":[{"url":"https:\/\/t.co\/WrmL4OVLCW","expanded_url":"https:\/\/twitter.com\/i\/web\/status\/1130715614992060416","display_url":"twitter.com\/i\/web\/status\/1\u2026","indices":[117,140]}],"user_mentions":[],"symbols":[]},"favorited":false,"retweeted":false,"filter_level":"low","lang":"en"},"is_quote_status":false,"quote_count":0,"reply_count":0,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[],"urls":[],"user_mentions":[{"screen_name":"LeeMcKenzieTV","name":"Lee McKenzie","id":21200516,"id_str":"21200516","indices":[3,17]}],"symbols":[]},"favorited":false,"retweeted":false,"filter_level":"low","lang":"en","timestamp_ms":"1558429074722"}```

Here's the corresponding output of [tweets_printer.py](tweets_printer.py):
```
1130759612280516608
Tue May 21 08:57:54 +0000 2019
RT @LeeMcKenzieTV: I never took for granted any chance to chat with Niki Lauda. When he spoke you listened. A true great, bravery beyond be…
845950663595085824
Elle
Es_Ellie_
```

The resulting entry in the json file created by [json_object_creator.py](json_object_creator.py):

```{"id": 1130759612280516608, "created_at": "Tue May 21 08:57:54 +0000 2019", "text": "RT @LeeMcKenzieTV: I never took for granted any chance to chat with Niki Lauda. When he spoke you listened. A true great, bravery beyond be\u2026", "user": {"id": 845950663595085824, "name": "Elle", "screen_name": "Es_Ellie_"}}```
