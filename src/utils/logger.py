import logging

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()

def log_info(message):
    """Log normal events"""
    logger.info(message)

def log_error(message):
    """Log errors"""
    logger.error(message)
