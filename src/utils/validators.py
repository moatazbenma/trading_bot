def validate_order(symbol, side, quantity, price=None):
    """
    Validate order parameters before sending to Binance
    """
    if not symbol.isalnum():
        raise ValueError("Invalid symbol format")
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")
    if price is not None and price <= 0:
        raise ValueError("Price must be greater than 0 for limit orders")
