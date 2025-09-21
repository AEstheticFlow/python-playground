# ----------------------------------------
# PyQt5 Example: Using QLabel in a QMainWindow
# ----------------------------------------

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont   # Used to change font family, size, weight, style
from PyQt5.QtCore import Qt     # Provides alignment and other constants


# ---------- Main Window Class ---------- #
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)   # x, y, width, height

        # --- Create a QLabel ---
        label = QLabel("Hello", self)          # Parent = MainWindow
        label.setFont(QFont("Arial", 40))      # Family, Size
        label.setGeometry(0, 0, 500, 100)      # x, y, width, height

        # --- Styling (CSS-like rules) ---
        label.setStyleSheet(
            "color: #292929;"            # Text color (hexadecimal)
            "background-color: #ab5c74;" # Background fill
            "font-weight: bold;"         # Bold text
            "font-style: italic;"        # Italics
            "text-decoration: underline;"# Underlined text
        )

        # --- Text Alignment (pick one) ---
        """Vertical alignment: """
        # label.setAlignment(Qt.AlignTop)
        # label.setAlignment(Qt.AlignBottom)
        # label.setAlignment(Qt.AlignVCenter)

        """Horizontal alignment: """
        # label.setAlignment(Qt.AlignLeft)
        # label.setAlignment(Qt.AlignRight)
        # label.setAlignment(Qt.AlignHCenter)

        """Combined alignment (bitwise OR: |)"""
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)      
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)   
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  
        # label.setAlignment(Qt.AlignCenter)   # Shortcut for horizontal + vertical center


# ---------- Entry Point ---------- #
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Core application loop
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())         # Ensures a clean exit when the GUI is closed

# NOTE:
# QFont("Arial", 40) → i can pass optional arguments (weight, italic) too.
#.setStyleSheet() → Works like CSS, very powerful for customizing PyQt widgets.
#.setAlignment(Qt.AlignCenter) → The most common case: center both horizontally and vertically.


# https://www.youtube.com/watch?v=nFLADhwXjW4&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=79