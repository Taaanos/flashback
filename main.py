import sys
from main_window import MainWindow
from PySide6.QtWidgets import QApplication
import logging
logger = logging.getLogger(__name__)

def main():
  logging.basicConfig(level=logging.INFO)
  logger.info("Starting the application")
  app = QApplication(sys.argv)
  widget = MainWindow()
  widget.show()
  sys.exit(app.exec())

if __name__ == "__main__":
  main()
