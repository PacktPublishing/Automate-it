from twython import Twython

APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN =''
OAUTH_TOKEN_SECRET = ''
twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Example 1
tweet = twitter.get_home_timeline()[1]
print "Tweet text: ", tweet["text"]
print "Tweet created at: ", tweet["created_at"]
print "Tweeted by: ", tweet["entities"]["user_mentions"][0]["name"]
print "Re Tweeted?: ", tweet["retweet_count"]

# Example 2
twitter.update_status(status='Python import antigravity https://xkcd.com/353/')




