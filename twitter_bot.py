import config
import tweepy
from binance.client import Client
from tkinter import*
from tkinter import ttk

auth = tweepy.AppAuthHandler(
    config.twitter_api_key, config.twitter_api_secret)

api = tweepy.API(auth)


def input_api_keys():
    window = Tk()
    window.title("ElonDoge Bot")
    window.geometry('325x350')
    window.configure(background="gray")

    api_key_label = Label(text="API Key")
    api_key_entry = Entry()
    api_secret_label = Label(text="API Secret")
    api_secret_entry = Entry()
    api_key_label.grid(row=0, column=0)
    api_key_entry.grid(row=0, column=1)
    api_secret_label.grid(row=0, column=2)
    api_secret_entry.grid(row=0, column=3)
    ttk.Button(window, text="Enter").grid(row=0, column=4)

    window.mainloop()


def input_phone_number():
    # Feature to add... let user choose between email/phone#/both
    pass


def last_elon_tweet():
    # Use twitter Api to constanly poll for new tweets
    new_tweet = None
    elon_tweets = api.user_timeline(screen_name="elonmusk", count=1)

    textonly_tweet = [tweet.text for tweet in elon_tweets]
    split_tweets = []
    for i in textonly_tweet:
        split_tweets.append(i.split())

    formatted_tweet = []
    for list_of_words in split_tweets:
        for word in list_of_words:
            if "@" not in word:
                formatted_tweet.append(word)
    last_tweet = " "
    last_tweet = last_tweet.join(formatted_tweet)

    return last_tweet


def check_tweet(tweet):
    assert isinstance(tweet, str)
    tweet = tweet.lower()
    if "doge" in tweet or "dogecoin" in tweet:
        return True
    else:
        return False


# when a new tweet is gotten, should update a list of past 5 tweets. before setting newTrade to True,
# check against past 5 tweets to make sure its not a glitch where its just
