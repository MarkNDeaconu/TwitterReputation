import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level

async def main():
    api = API()  # or API("path-to.db") - default is `accounts.db`

    # ADD ACCOUNTS (for CLI usage see BELOW)
    await api.pool.delete_accounts(["bobgorp", "gartmobile"])

    # await api.pool.add_account("bobgorp", "bobgorp00", "wopigir392@kvegg.com", "bobgorp00")
    # await api.pool.add_account("gartmobile", "md200300", "markdeaconu6@gmail.com", "md200300")
    # await api.pool.login_all()
    poop = await api.tweet_details(1878290215770509796)

    print(poop)
    # API USAGE

    # tweets = await gather(api.user_tweets(44196397, limit=10))
    
    # for i, tweet in enumerate(tweets, start=1):
    #     print(f"{i}. Tweet ID: {tweet.id}")
    #     print(f"   Username: {tweet.user.username}")
    #     print(f"   Text: {tweet.rawContent}\n")
    


if __name__ == "__main__":
    asyncio.run(main())