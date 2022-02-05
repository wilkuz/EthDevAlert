import requests
import tweepy
import json
import time
from dotenv import dotenv_values

# creates dictionary of keys stored in your .env file
keys = dotenv_values("credentials.env")

# loads credentials to constants
ETHERSCAN_API_KEY=keys["ETHERSCAN_API_KEY"]
TWITTER_API_KEY=keys["TWITTER_API_KEY"]
TWITTER_API_SECRET=keys['TWITTER_API_SECRET']
TWITTER_ACC_TOKEN=keys['TWITTER_ACC_TOKEN']
TWITTER_ACC_SECRET=keys['TWITTER_ACC_SECRET']
ETH_DEV_ADDRESS = "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe"


def get_txhash(address, key):
    tx_url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=120000&endblock=99999999&page=1&offset=10&sort=desc&apikey={key}"

    tx_list_response = requests.get(tx_url)
    print(tx_list_response)
    tx_json = tx_list_response.json()

    latest_txhash = tx_json["result"][0]["hash"]

    return latest_txhash




def get_balance(address, key):
    balance_url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={key}"

    balance_response = requests.get(balance_url)
    print(balance_response)
    json_response = balance_response.json()

    latest_balance = json_response["result"]
    latest_balance = int(latest_balance)

    return latest_balance




def tweet(latest_hash):
    # authenticate
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
    auth.set_access_token(TWITTER_ACC_TOKEN, TWITTER_ACC_SECRET)
    api = tweepy.API(auth)

    # content of new tweet
    post = f"The ETH balance on the ETH Dev contract just changed, see details of tx here: https://etherscan.io/tx/{latest_hash}"

    # send tweet
    api.update_status(post)



def main():
    # initiate balance and time
    starttime = time.time()
    latest_balance = get_balance(ETH_DEV_ADDRESS, ETHERSCAN_API_KEY)
    while True:
        new_balance = get_balance(ETH_DEV_ADDRESS, ETHERSCAN_API_KEY)
        
        # if the balance has changed, get the transaction and post a tweet
        if new_balance < latest_balance:
            latest_hash = get_txhash(ETH_DEV_ADDRESS, ETHERSCAN_API_KEY)
            tweet(latest_hash)
            latest_balance = new_balance
        time.sleep(14 - ((time.time() - starttime) % 14.0))

if __name__ == '__main__':
    main()
