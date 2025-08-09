from src.utils.binance_client import get_binance_client

client = get_binance_client()
print(client.futures_account_balance())
