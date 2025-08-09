import time
from src.utils.binance_client import get_binance_client
from src.utils.validators import validate_order
from src.utils.logger import log_info, log_error

def place_twap_order(symbol, side, total_quantity, interval_seconds, num_slices, order_type="MARKET", price=None):
    """
    Place a TWAP order by splitting total_quantity into smaller chunks.

    Args:
        symbol (str): Trading pair symbol
        side (str): "BUY" or "SELL"
        total_quantity (float): Total quantity to trade
        interval_seconds (int): Seconds to wait between each slice order
        num_slices (int): Number of slices to divide the order into
        order_type (str): "MARKET" or "LIMIT"
        price (float, optional): Price for LIMIT orders

    """
    try:
        validate_order(symbol, side, total_quantity)

        if total_quantity <= 0 or num_slices <= 0 or interval_seconds < 0:
            raise ValueError("Quantities, slices and interval must be positive")

        slice_qty = total_quantity / num_slices
        client = get_binance_client()

        log_info(f"Starting TWAP order: {side} {total_quantity} {symbol} in {num_slices} slices every {interval_seconds}s")

        for i in range(num_slices):
            log_info(f"Placing slice {i+1}/{num_slices} for {slice_qty} {symbol}")

            if order_type.upper() == "MARKET":
                order = client.futures_create_order(
                    symbol=symbol.upper(),
                    side=side.upper(),
                    type="MARKET",
                    quantity=slice_qty
                )
            elif order_type.upper() == "LIMIT":
                if price is None or price <= 0:
                    raise ValueError("Valid price must be provided for LIMIT orders")

                order = client.futures_create_order(
                    symbol=symbol.upper(),
                    side=side.upper(),
                    type="LIMIT",
                    timeInForce="GTC",
                    quantity=slice_qty,
                    price=str(price)
                )
            else:
                raise ValueError("Unsupported order type. Use MARKET or LIMIT.")

            log_info(f"TWAP slice order placed: {order}")
            print(f"✅ TWAP slice {i+1} order placed: {order}")

            if i < num_slices - 1:
                time.sleep(interval_seconds)

        log_info("TWAP order completed successfully.")

    except Exception as e:
        log_error(f"Error in TWAP order: {str(e)}")
        print("❌ Error placing TWAP order:", e)
