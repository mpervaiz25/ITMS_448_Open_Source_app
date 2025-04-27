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