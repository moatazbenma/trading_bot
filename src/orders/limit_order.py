from src.utils.binance_client import get_binance_client
from src.utils.validators import validate_order
from src.utils.logger import log_info, log_error

def place_limit_order(symbol, side, quantity, price, time_in_force="GTC"):
    """
    Place a limit order on Binance Futures Testnet
    """
    try:
        validate_order(symbol, side, quantity)

        if price <= 0:
            raise ValueError("Price must be positive")

        client = get_binance_client()

        log_info(f"Placing LIMIT {side} order: {symbol}, Qty: {quantity}, Price: {price}")

        order = client.futures_create_order(
            symbol=symbol.upper(),
            side=side.upper(),
            type="LIMIT",
            timeInForce=time_in_force,
            quantity=quantity,
            price=str(price)
        )

        log_info(f"Limit order placed successfully: {order}")
        print("✅ Limit order placed successfully!")
        print(order)

    except Exception as e:
        log_error(f"Error placing limit order: {str(e)}")
        print("❌ Error placing limit order:", e)
