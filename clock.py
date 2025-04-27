from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QButtonGroup


class Clock(QWidget):

    def __init__(self, main_window):
        super().__init__()

        #Variable declarations
        self.main_window = main_window
        self.vbox = QVBoxLayout(self)
        self.hbox = QHBoxLayout(self)
        self.display = QLabel(self)
        self.empty_field = QLabel(self)
        self.empty_field.setObjectName("empty_field") # Name for CSS styling
        self.timer = QTimer()
        self.button_group = QButtonGroup()
        self.button_clock = QPushButton("Clock", self)
        self.button_timer = QPushButton("Timer", self)
        self.window_width = 600
        self.window_height = 312
        self.monitor = QGuiApplication.primaryScreen().geometry()
        self.monitor_width = self.monitor.width()
        self.monitor_height = self.monitor.height()
        self.window_x = 0
        self.window_y = 0

        #Method calls
        self.initUI()

    def initUI(self):
        self.button_clock.setCheckable(True)
        self.button_timer.setCheckable(True)
        self.button_group.addButton(self.button_clock)
        self.button_group.addButton(self.button_timer)
        self.button_clock.setChecked(True)
        self.button_timer.setChecked(False)
        self.button_group.setExclusive(True)
        self.button_timer.clicked.connect(self.on_switch_button_pushed) #Don't forget to add only reference
        self.setWindowTitle("Digital clock and timer")
        self.window_x = int((self.monitor_width - self.frameSize().width()) / 2)
        self.window_y = int((self.monitor_height - self.frameSize().height()) / 2)
        self.setGeometry(self.window_x, self.window_y, self.window_width, self.window_height)
        self.setLayout(self.vbox)
        self.display.setText("00:00:00")
        self.display.setFixedHeight(140)
        self.empty_field.setFixedHeight(66)
        self.hbox.addWidget(self.button_clock)
        self.hbox.addWidget(self.button_timer)
        self.hbox.setAlignment(Qt.AlignTop)
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.display)
        self.vbox.addWidget(self.empty_field)
        self.timer.timeout.connect(self.update_display)
        self.timer.start(1000)
        self.display.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
            Clock{
                background-color: rgb(230, 230, 255);
            }
            QLabel, QPushButton{
                padding: 20px;
            }
            QLabel{
                font-size: 70px;
                font-family: code squared;
                font-weight: bold;
                color: rgb(50, 255, 50);
                background-color: black;
            }
            QPushButton{
                font-size: 20px;
                font-family: Bahnschrift;
                font-weight: bold;
            }
            QPushButton:hover{
                background-color: white;
                border-radius: 3px;
                border: 1px solid black
            }
            QLabel#empty_field{
                background-color: rgb(230, 230, 255);
            }
        """)


    def update_display(self):
        time = QTime.currentTime().toString("hh:mm:ss")
        self.display.setText(time)

    def on_switch_button_pushed(self):
        sender = self.sender()
        text = str(sender.text()).lower()

        if text == "timer":
            self.hide()
            self.main_window.timer_1.show()