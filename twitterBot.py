import tweepy
import metaphysic
import os
import sys
sys.path.insert(1, '/metaphysic')

from dotenv import load_dotenv
load_dotenv()

# API KEYS
bearer_token = os.getenv("BEARER_TOKEN") 
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET") 
access_token = os.getenv("ACCESS_TOKEN") 
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET") 

trigger_words = ['tengok', 'tarikh', 'lahir', 'analyze', 'tgk', 'analisa', 'analyse','dob']


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def cleanUpFile(filename):
    print('Clean up file!')
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("The file does not exist")

def upload_image_to_twitter(fileName):
    # Upload image to twitter and get media id
    with open(fileName, "rb") as tempFile:
        print('Uploading image to twitter')
        upload_result = api.chunked_upload(
            file=tempFile, filename=tempFile.name, media_category='tweet_image')
        return upload_result.media_id

def reply_mention(tweet):
    id = tweet['id']
    text = tweet['text']
    text = text.lower()
    # if(any(word in text for word in trigger_words)):
    splitted_word = text.split()
    for dob in splitted_word:
        if(metaphysic.check_input(dob)):
            print(f'reply mention to {id} with {dob}')
            input_array = list(map(str, dob))
            if dob[4:8] == "2000":
                input_array[4:8] = list("2005")
            image_name = metaphysic.begin_drawing(dob,input_array)
            media_id = upload_image_to_twitter(image_name)
            api.update_status(status=dob, in_reply_to_status_id=id, auto_populate_reply_metadata=True,media_ids=[media_id])
            cleanUpFile(image_name)
class Stream(tweepy.StreamingClient):
    def on_connect(self):
        print("Connected")

    def on_tweet(self, tweet):
        if tweet.data['author_id'] != '1111803728762302465':
            reply_mention(tweet.data)
        return

    def on_errors(self, errors):
        return super().on_errors(errors)


stream = Stream(bearer_token=bearer_token)
stream.add_rules(tweepy.StreamRule(value="@salemthecats"))
stream.filter(expansions="author_id")
