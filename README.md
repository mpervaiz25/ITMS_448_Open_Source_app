# ITMS_448_Open_Source_app

This project is our Python-based desktop application that tracks real-time Bitcoin market information.  
It displays the following live data inside a simple graphical user interface (GUI):
- Current Bitcoin Price (via CoinGecko API)
- Bitcoin Market Cap and 24h Volume (via CoinGecko API)
- Current Crypto Fear & Greed Index (via alternative.me API)
- Latest Bitcoin News Headline (via NewsAPI)

The application features a "Refresh" button to pull the latest data without restarting the app.

# Requirements

- `requests` library
- `python-dotenv` library
- Internet connection (to fetch live data)

You can install the required libraries by running the command below in your terminal/bash:

pip install -r requirements.txt