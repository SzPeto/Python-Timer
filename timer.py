import webbrowser

from PyQt5.QtCore import QTimer, QTime, Qt, QElapsedTimer
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QButtonGroup


class Timer(QWidget):

    def __init__(self, main_window):
        super().__init__()

        # Dependency
        self.main_window = main_window

        # Layouts
        self.vbox = QVBoxLayout(self)
        self.hbox = QHBoxLayout(self)
        self.hbox_2 = QHBoxLayout(self)
        self.hbox_support_me = QHBoxLayout()

        # Buttons
        self.button_group = QButtonGroup()
        self.button_clock = QPushButton("Clock", self)
        self.button_timer = QPushButton("Timer", self)
        self.button_start = QPushButton("Start", self)
        self.button_stop = QPushButton("Stop", self)
        self.button_reset = QPushButton("Reset", self)
        self.support_me_button = QPushButton("Support me")

        #Dimensions
        self.window_width = 600
        self.window_height = 370
        self.monitor = QGuiApplication.primaryScreen().geometry()
        self.monitor_width = self.monitor.width()
        self.monitor_height = self.monitor.height()
        self.window_x = 0
        self.window_y = 0

        # Other
        self.setWindowIcon(self.main_window.app_icon)
        self.display = QLabel(self)
        self.millisecond_save = 0
        self.timer = QTimer()
        self.elapsed_timer = QElapsedTimer()
        self.formatted_time = ""
        self.elapsed_msec = 0
        self.start_active = False

        #Method calls
        self.initUI()

    def initUI(self):
        # Buttons
        self.support_me_button.setObjectName("supportMeButton")
        self.button_clock.setCheckable(True)
        self.button_timer.setCheckable(True)
        self.button_group.addButton(self.button_clock)
        self.button_group.addButton(self.button_timer)
        self.button_group.setExclusive(True)
        self.button_clock.setChecked(False)
        self.button_timer.setChecked(True)

        # Dimensions and alignment
        self.window_x = int((self.monitor_width - self.frameSize().width()) / 2)
        self.window_y = int((self.monitor_height - self.frameSize().height()) / 2)
        self.setFixedSize(self.window_width, self.window_height)
        self.setGeometry(self.window_x, self.window_y, self.window_width, self.window_height)
        self.display.setFixedHeight(140)
        self.display.setAlignment(Qt.AlignCenter)

        # Layouts
        self.setLayout(self.vbox)
        self.hbox.addWidget(self.button_clock)
        self.hbox.addWidget(self.button_timer)
        self.hbox.setAlignment(Qt.AlignTop)
        self.hbox_2.addWidget(self.button_start)
        self.hbox_2.addWidget(self.button_stop)
        self.hbox_2.addWidget(self.button_reset)
        self.hbox_support_me.addWidget(self.support_me_button, alignment = Qt.AlignHCenter)
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.display)
        self.vbox.addLayout(self.hbox_2)
        self.vbox.addLayout(self.hbox_support_me)

        # Event handling and misc.
        self.timer.timeout.connect(self.update_display)
        self.button_clock.clicked.connect(self.on_switch_button_pushed)
        self.button_start.clicked.connect(self.start_timer)
        self.button_stop.clicked.connect(self.stop_timer)
        self.button_reset.clicked.connect(self.reset_timer)
        self.setWindowTitle("Digital clock and timer by Peter Szepesi")
        self.display.setText("00:00:00.00")
        self.support_me_button.clicked.connect(self.support_me)
        self.setStyleSheet("""
            Timer{
                background-color: rgb(230, 230, 255);
            }
            
            QLabel, QPushButton{
                padding: 20px;
            }
            
            QLabel{
                font-size: 80px;
                font-family: Consolas;
                font-weight: bold;
                color: rgb(50, 255, 50);
                background-color: black;
            }
            
            QPushButton{
                font-size: 20px;
                font-family: segoe UI;
                font-weight: bold;
            }
            
            QPushButton:hover{
                background-color: white;
                border-radius: 3px;
                border: 1px solid black
            }
            
            QPushButton#supportMeButton{
                font-size: 15px;
                font-family: Segoe UI;
                font-weight: normal;
                padding: 7px;
            }
            
        """)


    def update_display(self):
        self.display.setText(self.format_time())

    def on_switch_button_pushed(self):
        sender = self.sender()
        text = str(sender.text()).lower()

        if text == "clock":
            self.hide()
            self.main_window.clock_1.show()

        self.button_clock.setChecked(False)
        self.button_timer.setChecked(True)

    def start_timer(self):
        if not self.start_active:
            self.timer.start(10)
            self.elapsed_timer.start()
        self.start_active = True

    def stop_timer(self):
        self.start_active = False
        self.timer.stop()
        self.save_time()

    def reset_timer(self):
        self.start_active = False
        self.elapsed_timer.restart()
        self.display.setText("00:00:00.00")
        self.millisecond_save = 0

    def format_time(self):
        self.elapsed_msec = self.elapsed_timer.elapsed() + self.millisecond_save
        milliseconds = self.elapsed_msec % 1000 // 10
        seconds = self.elapsed_msec // 1000 % 60
        minutes = self.elapsed_msec // 1000 // 60 % 60
        hours = self.elapsed_msec // 1000 // 60 // 60
        self.formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"
        return self.formatted_time

    def save_time(self):
        self.millisecond_save = self.elapsed_msec

    def support_me(self):
        webbrowser.open("https://www.paypal.me/szpeto")