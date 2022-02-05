# ETHDEV TWITTER BOT

## The idea
The idea behind this project comes from an observation made by the crypto twitter community, as the Eth Dev contract often seem to make good trading decisions and selling near tops. I wanted to make a contribution to the community by creating a bot that alerts anyone following the account when there is a transaction made in the future.

The twitter account for this project can be found here: https://twitter.com/ethdevalert


## What it does
This python application will post a tweet-alert when it gets information from the etherscan API about a change in balance of the Eth dev contract. It uses both twitter and etherscan API. It requires a developer-account on twitter with elevated access. 
https://developer.twitter.com/en
https://etherscan.io/apis

The application makes a request every 14 seconds, which matches the ~14 second block time on the ethereum blockchain.
This should ensure an update every block, and as the current balance of the ETH dev contract is used to detect a change, there is very little risk of missing a transfer of funds with this method.
The possible lag of a tweet from the actual transaction finalization is not very important.

## Usage

### EthDevAlert.py contains three functions and a main function. Two of the three functions defined are related to etherscan:

the `get_balance(address, key)` function takes an ethereum address and etherscan API-key and returns the current ETH balance of the address on the blockchain. This function is used to detect change in the Eth Dev contract.


the `get_txhash(address, key)` function takes and ethereum address and etherscan API-key and returns the transaction hash for the latest transaction made by the address.


The third function, `tweet(latest_hash)` takes a transaction hash as input and posts a tweet using the tweepy package.


The program functions as following: the `main()` function initiates the current balance and calls for a balance update every 14 seconds. After each update it checks if the balance has changed. If it has changed it will post a tweet
including the transaction hash of the latest transaction made by the contract.

### What I learned

Interacting with API:s in python
Using environment values for security
Using twitter API:s
How to interpret different transaction types on the ethereum blockchain
