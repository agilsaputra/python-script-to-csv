import tweepy
import csv

# Authenticate with Twitter API
consumer_key = 'imuI1TDds3LwklUnu6StMObR7'
consumer_secret = 'In1hcnJYIIJjmx3G2SZXWOca1N0cW6wgRTOn6v7qeE9buU24P3'
access_token = '1613473924981092353-dsSzyzmu4ATYMrbrMmRZslJTIQPuw0'
access_token_secret = 'foZVw5Z6IZ7DmVBF5479mKzTFhEeSMXj2cp9G3l2oHfsF'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Search for tweets containing the word "Python" and items is for limit tweet pull
tweets = []
for tweet in tweepy.Cursor(api.search_tweets, q='papua', lang='en').items(2):
    tweets.append(tweet)
    print(tweet.text)

# Open a CSV file to store the tweets
with open('tweets.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'created_at', 'text']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Iterate through the tweets and save them to the CSV file
    for tweet in tweets:
        writer.writerow({'id': tweet.id, 'created_at': tweet.created_at, 'text': tweet.text})

print("Finished writing tweets to CSV file.")

