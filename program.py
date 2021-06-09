import twitter_bot
import trade_bot
import time


def main():
    # Boolean set to true when it is determined there is a new tweet

    newTweet = False

    while True:
        last_tweet = twitter_bot.last_elon_tweet()

        newTweet = twitter_bot.check_tweet(last_tweet)

        if newTweet:
            twitter_bot.place_trade()
        else:
            print("No new tweets. \n Last Tweet: \"" + last_tweet + " \"")
        time.sleep(1)
    tweet = None
    print(last_tweet)


if __name__ == "__main__":
    main()
