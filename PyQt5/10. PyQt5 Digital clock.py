# -----------------------------
# PyQt5 Digital Clock Example
# -----------------------------
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()

        # --- Widgets ---
        self.time_label = QLabel(self)   # Label that will display the time
        self.timer = QTimer(self)        # Timer that updates the clock every second

        self.initUI()

    def initUI(self):
        """Initializes the UI for the clock window."""
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 100)  # x-pos, y-pos, width, height

        # --- Layout ---
        # Vertical layout to center the label inside the window
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        # --- Label Styling ---
        self.time_label.setAlignment(Qt.AlignCenter)   # Center horizontally + vertically
        self.time_label.setStyleSheet("font-size: 150px; color: hsl(111, 100%, 50%);")
        self.setStyleSheet("background-color: black;") # Window background color

        # --- Custom Font ---
        # Load a custom .TTF font (Digital style numbers)
        font_id = QFontDatabase.addApplicationFont(
            "C:/Users/A.R/Documents/PROGRAMMING/pythonData/Media/DS-DIGIT.TTF"
        )
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)  # Apply custom font, with size 150
        self.time_label.setFont(my_font)

        # --- Timer ---
        # Connect QTimer to update_time() so the label refreshes every second
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # 1000 ms = 1 second

        # Update immediately (so it doesn’t wait 1 sec to display the first time)
        self.update_time()

    def update_time(self):
        """Updates the label with the current system time."""
        # Format: hh:mm:ss AM/PM
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)


# -----------------------------
# Application Entry Point
# -----------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())


# https://www.youtube.com/watch?v=543g1CurFFo&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=87