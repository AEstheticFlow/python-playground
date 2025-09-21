import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("PyQt5 QLineEdit Example")

        # --- Widgets ---
        self.line_edit = QLineEdit(self)           # Input box
        self.button = QPushButton("Submit", self)  # Button

        self.initUI()

    def initUI(self):
        # --- Position and Size ---
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.button.setGeometry(220, 10, 100, 40)

        # --- Style ---
        self.line_edit.setStyleSheet(
            "font-size: 25px;"
            "font-family: Arial;"
        )
        self.button.setStyleSheet(
            "font-size: 25px;"
            "font-family: Arial;"
        )

        # --- Placeholder (grayed-out hint text inside QLineEdit) ---
        self.line_edit.setPlaceholderText("Enter your name")

        # --- Connect button click to slot ---
        # When clicked → runs self.submit()
        self.button.clicked.connect(self.submit)

    # --- Slot (what happens on submit) ---
    def submit(self):
        # .text() retrieves whatever the user typed in
        text = self.line_edit.text()
        # For now, just printing to console
        print(f"Hello {text}")


# --- Entry Point ---
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


# https://www.youtube.com/watch?v=4IUWg_wQNSc&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=85