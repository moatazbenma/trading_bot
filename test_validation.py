from src.utils.validators import validate_order

try:
    validate_order("BTCUSDT", "BUY", 0.01)  
    print("Validation passed ✅")
except ValueError as e:
    print("Validation failed ❌:", e)

try:
    validate_order("BTC_USDT", "BUY", 0.01)  
except ValueError as e:
    print("Validation failed as expected:", e)
