# ---------------- PYQT5 INTRODUCTION ---------------- #
# Goal: Create a simple GUI window using PyQt5.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow   # Core GUI components
from PyQt5.QtGui import QIcon                           # To set a window icon


# ---------------- MAIN WINDOW CLASS ---------------- #
class MainWindow(QMainWindow):      # `self`` here always refers to my main window
    def __init__(self):
        super().__init__()          # Initialize the parent class (QMainWindow)

        # ----- WINDOW SETTINGS -----
        self.setWindowTitle("My Cool First GUI")   # Title bar text

        # Position & size: (x-position, y-position, width, height)
        self.setGeometry(700, 300, 500, 500)

        # Add a custom icon (must be a valid image file: .png, .ico, etc.)
        self.setWindowIcon(QIcon("C:/Users/A.R/Documents/PROGRAMMING/pythonData/Media/my_GUI_pic.jpg"))


# ---------------- APPLICATION ENTRY POINT ---------------- #
if __name__ == "__main__":
    # QApplication: Manages the GUI application's control flow & settings.
    # sys.argv: Passes command-line arguments to the app (needed for Qt).
    app = QApplication(sys.argv)

    # Create our main window (instance of MainWindow)
    window = MainWindow()
    window.show()   # Show the window on screen

    # Start the application event loop (keeps the app running until closed).
    # sys.exit ensures a clean exit code is returned.
    sys.exit(app.exec_())

# https://www.youtube.com/watch?v=Uvqmv3PGiXM&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=78