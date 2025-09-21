import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)          # x, y, width, height
        self.setWindowTitle("PyQt5 Button Example")

        # --- Widgets ---
        self.button = QPushButton("Click me!", self)  # Button widget
        self.label = QLabel("Hello", self)            # Label widget

        self.initUI()

    def initUI(self):
        # --- Button Setup ---
        self.button.setGeometry(150, 200, 200, 100)   # x, y, w, h
        self.button.setStyleSheet("font-size: 30px;")

        # "clicked" is a SIGNAL that QPushButton emits when pressed
        # We connect it to our own SLOT (the `on_click` method) and execute it
        self.button.clicked.connect(self.on_click)

        # --- Label Setup ---
        self.label.setGeometry(200, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px;")


    def on_click(self):
        """Slot method: gets executed when button is clicked."""
        print("Button clicked!")

        # Change button text
        self.button.setText("Clicked!!")

        # Disable button so it can’t be pressed again
        self.button.setDisabled(True)

        # Update label text
        self.label.setText("Bye")


# -------- Entry Point --------
if __name__ == '__main__':
    app = QApplication(sys.argv)   # Creates application loop
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())          # Ensures proper exit


# https://www.youtube.com/watch?v=9pl55MxZlG4&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=82