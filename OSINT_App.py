import tkinter as tk
from tkinter import ttk
import requests
import threading
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# API URLs
COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
COINCAP_URL = "https://api.coingecko.com/api/v3/coins/bitcoin"
FEAR_GREED_URL = "https://api.alternative.me/fng/"
NEWS_API_KEY = os.getenv("NEWS_API_KEY") 
NEWS_API_URL = f"https://newsapi.org/v2/everything?q=bitcoin&sortBy=publishedAt&language=en&pageSize=1&apiKey={NEWS_API_KEY}"

# Functions to fetch data from urls
def get_bitcoin_price():
    try:
        res = requests.get(COINGECKO_URL, timeout=5)
        res.raise_for_status()
        price = res.json()["bitcoin"]["usd"]
        return f"${price:,.2f}"
    except Exception as e:
        return f"Price error: {e}"

def get_market_data():
    try:
        res = requests.get(COINCAP_URL, timeout=5)
        res.raise_for_status()
        data = res.json()["market_data"]
        cap = data["market_cap"]["usd"]
        volume = data["total_volume"]["usd"]
        return f"Market Cap: ${cap:,.0f}\n24h Volume: ${volume:,.0f}"
    except Exception as e:
        return f"Market data error: {e}"

def get_fear_greed_index():
    try:
        res = requests.get(FEAR_GREED_URL, timeout=5)
        res.raise_for_status()
        data = res.json()["data"][0]
        return f"Fear & Greed Index: {data['value']} ({data['value_classification']})"
    except Exception as e:
        return f"FGI error: {e}"
    
def get_bitcoin_news():
    try:
        res = requests.get(NEWS_API_URL, timeout=5)
        res.raise_for_status()
        article = res.json()["articles"][0]
        return f"News: {article['title']}"
    except Exception as e:
        return f"News error: {e}"
    
# GUI updater

def update_all_data():
    refresh_btn.config(state="disabled", text="Refreshing...")
    price_label.config(text="Fetching price...")
    cap_label.config(text="Fetching market cap...")
    fear_label.config(text="Fetching sentiment...")
    news_label.config(text="Fetching news...")

    def task():
        price = get_bitcoin_price()
        market = get_market_data()
        fear = get_fear_greed_index()
        news = get_bitcoin_news()

        root.after(0, lambda: price_label.config(text=price))
        root.after(0, lambda: cap_label.config(text=market))
        root.after(0, lambda: fear_label.config(text=fear))
        root.after(0, lambda: news_label.config(text=news))
        root.after(0, lambda: refresh_btn.config(state="normal", text="Refresh"))

    threading.Thread(target=task).start()