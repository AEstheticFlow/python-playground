# -----------------------------
# PyQt5 Stopwatch Example
# -----------------------------
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, 
    QVBoxLayout, QHBoxLayout
)
from PyQt5.QtCore import QTimer, QTime, Qt


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()

        # --- Core Data ---
        self.time = QTime(0, 0, 0, 0)    # Internal stopwatch time
        self.timer = QTimer(self)        # Timer that ticks every 10 ms

        # --- Widgets ---
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)

        self.initUI()

    def initUI(self):
        """Initializes the stopwatch interface."""
        self.setWindowTitle("Stopwatch")

        # --- Layout Setup ---
        vbox = QVBoxLayout()            # Main vertical layout
        vbox.addWidget(self.time_label)

        hbox = QHBoxLayout()            # Row of buttons
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)
        self.setLayout(vbox)

        # --- Styling ---
        self.time_label.setAlignment(Qt.AlignCenter)

        self.setStyleSheet("""
            QPushButton, QLabel {
                padding: 20px;
                font-weight: bold;
                font-family: Calibri;
            }
            QPushButton {
                font-size: 60px;
            }
            QLabel {
                font-size: 150px;
                background-color: hsl(335, 91%, 58%);
                border-radius: 50px;
            }
        """)

        # --- Signal Connections ---
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    # -----------------------------
    # Stopwatch Core Functions
    # -----------------------------
    def start(self):
        """Starts the stopwatch (ticks every 10ms)."""
        self.timer.start(10)

    def stop(self):
        """Pauses the stopwatch."""
        self.timer.stop()

    def reset(self):
        """Stops and resets the stopwatch to 0."""
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))


    def format_time(self, time):
        """Formats QTime → hh:mm:ss.ms"""
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10   # Only show 2-digit milliseconds
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        """Updates the label every 10 ms while running."""
        self.time = self.time.addMSecs(10)  # Increment by 10 ms
        self.time_label.setText(self.format_time(self.time))


# -----------------------------
# Application Entry Point
# -----------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())
