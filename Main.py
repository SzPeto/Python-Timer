import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

class Main:

    def __init__(self):
        from clock import Clock
        from timer import Timer
        self.app_icon = QIcon(self.resource_path("stopwatch.png"))
        self.clock_1: Clock
        self.timer_1: Timer
        self.timer_1 = Timer(self) # DI - Dependency injection, we pass the reference to constructor
        self.clock_1 = Clock(self, self.timer_1)  # DI - Dependency injection, we pass the reference to constructor
        self.clock_1.show()

    def resource_path(self, relative_path):
        if hasattr(sys, "_MEIPASS"):
            return os.path.join(sys._MEIPASS, relative_path)  # In case of exe return the absolute path
        else:
            return os.path.join(os.path.abspath("."), relative_path)  # In case of IDE return the relative path

def main():
    app = QApplication(sys.argv)
    Main()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()