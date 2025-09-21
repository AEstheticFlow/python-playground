# ----------------------------------------
# PyQt5 Example: Displaying Images with QLabel
# ----------------------------------------

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap


# ---------- Main Window ---------- #
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)    # x, y, width, height
        self.setWindowTitle("Image Example")

        # --- QLabel to hold the image ---
        label = QLabel(self)                    # Parent = MainWindow
        label.setGeometry(0, 0, 500, 500)       # Same size as the window

        # --- Load image into a QPixmap ---
        pixmap = QPixmap("C:/Users/A.R/Documents/PROGRAMMING/pythonData/Media/my_GUI_pic.jpg")
        label.setPixmap(pixmap)

        # --- Scale image to fit label size ---
        label.setScaledContents(True)

        # OPTIONAL: manually center label in the window
        # (Not really needed since it fills the window here)
        label.setGeometry(
            (self.width() - label.width()) // 2,     # X position
            (self.height() - label.height()) // 2,   # Y position
            label.width(),
            label.height()
        )


# ---------- Entry Point ---------- #
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


# https://www.youtube.com/watch?v=7v5NQeIBYes&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=81