import requests
import random
import datetime

def get_btc():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd&include_24hr_change=true"
    data = requests.get(url).json()
    return data

def get_news():
    rss = "https://news.google.com/rss/search?q=crypto+market"
    return rss

def generate_tweet():
    data = get_btc()
    btc = data["bitcoin"]["usd"]
    btc_ch = round(data["bitcoin"]["usd_24h_change"], 2)
    eth = data["ethereum"]["usd"]
    eth_ch = round(data["ethereum"]["usd_24h_change"], 2)

    templates = [
        f"📊 Market Update:\nBTC: ${btc} ({btc_ch}%)\nETH: ${eth} ({eth_ch}%)\n#Crypto #Trading #SenseMarket",
        f"🚨 Crypto Pulse:\nBitcoin at ${btc} ({btc_ch}%)\nEthereum at ${eth} ({eth_ch}%)\nStay sharp. #Markets",
        f"📈 Traders watch this:\nBTC ${btc} | ETH ${eth}\nVolatility creates opportunity. #TradingTips"
    ]

    return random.choice(templates)

tweet = generate_tweet()

with open("tweet.txt", "w", encoding="utf-8") as f:
    f.write(tweet)

print("Generated tweet:")
print(tweet)
