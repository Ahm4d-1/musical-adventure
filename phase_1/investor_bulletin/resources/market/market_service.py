""" Market Service """
"""_summary_
this file to write any business logic for the Market
"""
import os
import requests

from resources.market.market_schema import MarketData

API_KEY = os.environ.get("TWELEVDATA_API_KEY")
BASE_URL = "https://api.twelvedata.com/price"

def get_market_data():
    symbols = ["AAPL", "MSFT", "GOOG", "AMZN", "META"]
    symbols_str = ",".join(symbols)

    response = requests.get(f"{BASE_URL}?symbol={symbols_str}&apikey={API_KEY}")

    prices = {}
    if response.status_code == 200:
        data = response.json()
        for symbol in symbols:
            prices[symbol] = data.get(symbol, {}).get("price")

    return MarketData(**prices)
