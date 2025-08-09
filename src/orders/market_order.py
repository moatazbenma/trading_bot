from src.utils.binance_client import get_binance_client
from src.utils.validators import validate_order
from src.utils.logger import log_info, log_error

def place_market_order(symbol, side, quantity):
    """
    Place a market order on Binance Futures Testnet
    """
    try:
        validate_order(symbol, side, quantity)

        client = get_binance_client()

        log_info(f"Placing MARKET {side} order: {symbol}, Qty: {quantity}")

        order = client.futures_create_order(
            symbol=symbol.upper(),
            side=side.upper(),
            type="MARKET",
            quantity=quantity
        )

        log_info(f"Order placed successfully: {order}")
        print("✅ Order placed successfully!")
        print(order)

    except Exception as e:
        log_error(f"Error placing order: {str(e)}")
        print("❌ Error placing order:", e)
