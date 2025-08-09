import time
from src.utils.binance_client import get_binance_client
from src.utils.validators import validate_order
from src.utils.logger import log_info, log_error

def place_grid_orders(symbol, side, total_quantity, grid_size, price_step, order_type="LIMIT", time_in_force="GTC"):
    """
    Place multiple limit orders spaced by price_step to create a grid.

    Args:
        symbol (str): Trading pair symbol
        side (str): "BUY" or "SELL"
        total_quantity (float): Total quantity to distribute among grid orders
        grid_size (int): Number of grid levels/orders
        price_step (float): Price difference between each grid level
        order_type (str): Order type, usually "LIMIT"
        time_in_force (str): Time in force for limit orders

    """
    try:
        validate_order(symbol, side, total_quantity)

        if total_quantity <= 0 or grid_size <= 0 or price_step <= 0:
            raise ValueError("Quantity, grid_size, and price_step must be positive")

        client = get_binance_client()

        slice_qty = total_quantity / grid_size

        ticker = client.futures_symbol_ticker(symbol=symbol.upper())
        current_price = float(ticker['price'])

        log_info(f"Placing grid orders around {current_price} for {symbol}")

        for i in range(grid_size):
            if side.upper() == "BUY":
                price = current_price - (price_step * (i + 1))
            else:  
                price = current_price + (price_step * (i + 1))

            log_info(f"Placing grid {side} order {i+1}/{grid_size} at price {price} qty {slice_qty}")

            order = client.futures_create_order(
                symbol=symbol.upper(),
                side=side.upper(),
                type=order_type,
                timeInForce=time_in_force,
                quantity=slice_qty,
                price=f"{price:.2f}"
            )

            log_info(f"Grid order placed: {order}")
            print(f"✅ Grid order {i+1} placed at {price} qty {slice_qty}")

            time.sleep(1)  

        log_info("All grid orders placed successfully.")

    except Exception as e:
        log_error(f"Error placing grid orders: {str(e)}")
        print("❌ Error placing grid orders:", e)
