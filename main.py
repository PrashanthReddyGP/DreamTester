"""
Main entry point for the Trade Backtesting Application.

Initializes the environment, sets up the Binance API client,
and launches the PySide6 GUI application.
"""

import os
import sys
import logging

from dotenv import load_dotenv
from binance.um_futures import UMFutures
from PySide6.QtWidgets import QApplication, QMessageBox

import utils  # Initialization import - performs setup actions on import.
from classes import backtester

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from .env file
load_dotenv()

# --- Environment Variable Check ---
api_key: str | None = os.environ.get("BINANCE_API")
api_secret: str | None = os.environ.get("BINANCE_SECRET")

if not api_key or not api_secret:

    error_message = "Error: BINANCE_API or BINANCE_SECRET environment variables not set.\nPlease ensure they are defined in your .env file or system environment."
    print(error_message) # Also print to console in case GUI fails

    sys.exit(1) # Exit if keys are missing

# --- Main Application Execution ---
if __name__ == "__main__":
    
    logging.info("Starting PySide6 application...")
    app: QApplication = QApplication(sys.argv)

    # --- Binance Client Initialization ---
    try:
        client: UMFutures = UMFutures(key=api_key, secret=api_secret)
        # Test connection or fetch basic account info
        client.get_account_trades(symbol='BTCUSDT', limit=1) # Example check
        logging.info("Binance UMFutures client initialized successfully.")

    except Exception as e:
        # Handle potential exceptions during client initialization or connection test
        error_message = f"Failed to initialize or connect Binance client: {e}"
        logging.error(error_message)
        # Again, ideally show this in a GUI message box if possible.
        print(error_message)
        sys.exit(1)

    try:
        widget: backtester.Backtester = backtester.Backtester(client=client)
        widget.show()
        logging.info("Backtester widget displayed.")
        sys.exit(app.exec())

    except Exception as e:
        logging.exception("An error occurred during application execution.")
        # Show error in a message box before exiting
        QMessageBox.critical(None, "Application Error", f"An unexpected error occurred: {e}")
        sys.exit(1)
