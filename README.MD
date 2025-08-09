# Binance Futures Trading Bot

A Python-based command-line trading bot for Binance USDT-M Futures on the Binance Futures Testnet.  
Supports multiple order types including Market, Limit, TWAP (Time-Weighted Average Price), and Grid Orders.  
Includes robust input validation, structured logging, and modular code design for easy extension.

---

## Setup Instructions
1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/yourname-binance-bot.git
   cd yourname-binance-bot

2. **Create and activate a virtual environment :**
python -m venv venv
source venv/bin/activate       # On Windows use: venv\Scripts\activate

3. **Install dependencies:**

pip install -r requirements.txt


4. **Configure environment variables:**
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here


## Usage

Run the test scripts to verify each order type functionality on Binance Futures Testnet.

| Test Script             | Description                              |
|-------------------------|------------------------------------------|
| `test_market_order.py`  | Tests placing a Market Order              |
| `test_limit_order.py`   | Tests placing a Limit Order               |
| `test_twap_order.py`    | Tests placing a TWAP Order (time-sliced) |
| `test_grid_orders.py`   | Tests placing multiple Grid Orders        |


## Logging

All bot activities, order placements, and errors are 
logged to bot.log with timestamps for traceability.

## License
This project is licensed under the MIT License.
