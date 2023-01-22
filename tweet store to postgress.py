import tweepy
import psycopg2

# Authenticate with Twitter API
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Search for tweets containing the word "Python"
tweets = []
for tweet in tweepy.Cursor(api.search_tweets, q='Python', lang='en').items(50):
    tweets.append(tweet)
    print(tweet.text)

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="your_host",
    port="your_port",
    user="your_user",
    password="your_password",
    database="your_database"
)

# Create a cursor object
cur = conn.cursor()

# Create the tweets table
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS tweets (
        id SERIAL PRIMARY KEY,
        tweet_id BIGINT NOT NULL,
        created_at TIMESTAMP NOT NULL,
        text TEXT NOT NULL
    )
    """
)
conn.commit()

# Iterate through the tweets and insert them into the tweets table
for tweet in tweets:
    cur.execute(
        """
        INSERT INTO tweets (tweet_id, created_at, text)
        VALUES (%s, %s, %s)
        """,
        (tweet.id, tweet.created_at, tweet.text)
    )

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

print("Finished writing tweets to the database.")

