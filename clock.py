import os
import sys
import webbrowser

from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QButtonGroup


class Clock(QWidget):

    def __init__(self, main_window, timer_window):
        super().__init__()

        #Variable declarations

        # Dependencies
        self.main_window = main_window
        self.timer_window = timer_window

        # Layouts
        self.v_box = QVBoxLayout(self)
        self.h_box = QHBoxLayout(self)
        self.h_box_support_me = QHBoxLayout()

        # Buttons
        self.button_group = QButtonGroup()
        self.button_clock = QPushButton("Clock", self)
        self.button_timer = QPushButton("Timer", self)
        self.support_me_button = QPushButton("Support me")

        # Dimensions
        self.window_width = 600
        self.window_height = 370
        self.monitor = QGuiApplication.primaryScreen().geometry()
        self.monitor_width = self.monitor.width()
        self.monitor_height = self.monitor.height()
        self.window_x = 0
        self.window_y = 0

        # Other
        self.timer = QTimer()
        self.empty_field_height = 66
        self.display = QLabel(self)
        self.empty_field = QLabel(self)
        self.empty_field.setObjectName("empty_field")  # Name for CSS styling

        #Method calls
        self.initUI()

    def initUI(self):

        # Buttons
        self.support_me_button.setObjectName("supportMeButton")
        self.button_clock.setCheckable(True)
        self.button_timer.setCheckable(True)
        self.button_group.addButton(self.button_clock)
        self.button_group.addButton(self.button_timer)
        self.button_clock.setChecked(True)
        self.button_timer.setChecked(False)
        self.button_group.setExclusive(True)

        # Dimensions and alignment
        self.window_x = int((self.monitor_width - self.frameSize().width()) / 2)
        self.window_y = int((self.monitor_height - self.frameSize().height()) / 2)
        self.setFixedSize(self.window_width, self.window_height)
        self.setGeometry(self.window_x, self.window_y, self.window_width, self.window_height)
        self.display.setFixedHeight(140)
        self.empty_field.setFixedHeight(self.empty_field_height)

        # Layouts
        self.setLayout(self.v_box)
        self.h_box.addWidget(self.button_clock)
        self.h_box.addWidget(self.button_timer)
        self.h_box_support_me.addWidget(self.support_me_button, alignment = Qt.AlignHCenter)
        self.v_box.addLayout(self.h_box)
        self.v_box.addWidget(self.display, alignment = Qt.AlignTop)
        self.v_box.addWidget(self.empty_field)
        self.v_box.addLayout(self.h_box_support_me)
        self.display.setAlignment(Qt.AlignCenter)

        # Event handling and other
        self.setWindowIcon(self.main_window.app_icon)
        self.timer.timeout.connect(self.update_display)
        self.button_timer.clicked.connect(self.on_switch_button_pushed)  # Don't forget to add only reference
        self.timer.start(1000)
        self.setWindowTitle("Digital clock and timer by Peter Szepesi")
        self.display.setText("00:00:00")
        self.support_me_button.clicked.connect(self.support_me)
        self.setStyleSheet("""
            Clock{
                background-color: rgb(230, 230, 255);
            }
            
            QLabel, QPushButton{
                padding: 20px;
            }
            
            QLabel{
                font-size: 100px;
                font-family: segoe UI;
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
            
            QLabel#empty_field{
                background-color: rgb(230, 230, 255);
            }
            
        """)


    def update_display(self):
        time = QTime.currentTime().toString("hh:mm:ss")
        self.display.setText(time)
        self.empty_field_height = self.timer_window.hbox_2.geometry().height()
        self.empty_field.setFixedHeight(self.empty_field_height)

    def on_switch_button_pushed(self):
        sender = self.sender()
        text = str(sender.text()).lower()

        if text == "timer":
            self.hide()
            self.main_window.timer_1.show()

        self.button_clock.setChecked(True)
        self.button_timer.setChecked(False)

    def support_me(self):
        webbrowser.open("https://www.paypal.me/szpeto")