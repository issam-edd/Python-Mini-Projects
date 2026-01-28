import tweepy

auth = tweepy.OAuthHandler('NwofzO56plq23QNa7j2r84Aid', '1OCVxBKvQdAY36x5IV8E1d2gSwb1K9Eflkw1Iuf1vQhvy4GElT')
auth.set_access_token('3092452577-0HNuVXLoCb8jSmixQAAJSbaQdjFxVyNTsFwbUJ4', '8HepQO4vOMoOmoLARROVNdLht0BXZiY4NiFUvc4thTYTN')
#berear token = AAAAAAAAAAAAAAAAAAAAALhBWAEAAAAAVYYUyNwNYmGu%2BAvZfSTp7bkkp%2Bo%3DyksQonSENnTehosiCxAZuJoAiO7LncDQhcpnuAY8gauhPp6035
api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)