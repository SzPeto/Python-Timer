import sys
from PyQt5.QtWidgets import QApplication

class Main:

    def __init__(self):
        from clock import Clock
        from timer import Timer
        self.timer_1 = Timer(self) # DI - Dependency injection, we pass the reference to constructor
        self.clock_1 = Clock(self, self.timer_1)  # DI - Dependency injection, we pass the reference to constructor
        self.timer_1.show()
        self.timer_1.hide()
        self.clock_1.show()

def main():
    app = QApplication(sys.argv)
    main_app = Main()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()