from binance.client import Client
import os
import time
from dotenv import load_dotenv

load_dotenv()

def get_binance_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    client = Client(api_key, api_secret, testnet=True)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    server_time = client.get_server_time()
    client.timestamp_offset = server_time['serverTime'] - int(round(time.time() * 1000))

    return client
