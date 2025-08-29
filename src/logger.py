import logging
import os
from datetime import datetime

# Create logs folder if not exists
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Log file name with timestamp
LOG_FILE = os.path.join(LOG_DIR, f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log")

# Create logger
logger = logging.getLogger("MLProjectLogger")
logger.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")

# File handler
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Optional: also print to console
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

logger.info(f"Logger initialized. Log file: {LOG_FILE}")
