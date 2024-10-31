import sys
from PyQt6.QtWidgets import QApplication
from gui.main_window import McSAS3MainWindow
import logging
from utils.logging_config import setup_logging

def main():
    # Initialize logging
    logger = setup_logging(log_level=logging.DEBUG, log_to_file=True)  # Enable file logging if needed
    logger.debug("Starting McSAS3 GUI application...")

    app = QApplication(sys.argv)
    main_window = McSAS3MainWindow()
    main_window.show()

    logger.debug("McSAS3 GUI is now visible.")
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
