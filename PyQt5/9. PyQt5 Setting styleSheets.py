import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 setStyleSheet Example")

        # --- Widgets ---
        # Notice: no parent (self) is passed, because the layout
        # will handle widget ownership + positioning.
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")

        # --- Central Widget ---
        # In QMainWindow, you MUST set a central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.initUI()

    def initUI(self):
        # --- Layout ---
        hbox = QHBoxLayout()            # Horizontal layout
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        # Apply layout to central widget
        self.central_widget.setLayout(hbox)

        # --- Object Names ---
        # Needed to target specific widgets in setStyleSheet()
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        # --- Global StyleSheet ---
        # Styles apply to all widgets of that type,
        # unless overridden by objectName selectors.
        self.setStyleSheet("""
            QPushButton{
                font-size: 40px;
                font-family: Arial;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 15px;
            }
            QPushButton#button1{
                background-color: hsl(0, 100%, 64%);
            }
            QPushButton#button2{
                background-color: hsl(122, 100%, 64%);
            }
            QPushButton#button3{
                background-color: hsl(204, 100%, 64%);
            }
            QPushButton#button1:hover{
                background-color: hsl(0, 100%, 84%);
            }
            QPushButton#button2:hover{
                background-color: hsl(122, 100%, 84%);
            }
            QPushButton#button3:hover{
                background-color: hsl(204, 100%, 84%);
            }
        """)


# --- Entry Point ---
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


# https://www.youtube.com/watch?v=YJM9d0F3n-o&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=86
