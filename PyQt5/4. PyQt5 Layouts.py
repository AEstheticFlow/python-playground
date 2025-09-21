# ---------------------------------------------------
# PyQt5 Layout Managers Example
# ---------------------------------------------------
# Layout managers automatically arrange widgets inside a window.
# Instead of using fixed .setGeometry(), layouts make the UI flexible
# and responsive to resizing.

import sys
from PyQt5.QtWidgets import(
    QApplication, QMainWindow, QLabel, QWidget,
    QVBoxLayout, QHBoxLayout, QGridLayout
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("Layout Managers Example")

        # --- Central widget acts as a container for layouts ---
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.initUI()

    def initUI(self):
        # --- Example widgets (colored labels) ---
        label1 = QLabel("#1")
        label2 = QLabel("#2")
        label3 = QLabel("#3")
        label4 = QLabel("#4")
        label5 = QLabel("#5")

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: purple;")

        # ------------------------------
        """VERTICAL LAYOUT (top → bottom)"""
        # ------------------------------
        # vbox = QVBoxLayout()
        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)
        # self.central_widget.setLayout(vbox)

        # ------------------------------
        """HORIZONTAL LAYOUT (left → right)"""
        # ------------------------------
        # hbox = QHBoxLayout()
        # hbox.addWidget(label1)
        # hbox.addWidget(label2)
        # hbox.addWidget(label3)
        # hbox.addWidget(label4)
        # hbox.addWidget(label5)
        # self.central_widget.setLayout(hbox)

        # ------------------------------
        """GRID LAYOUT (rows & columns)"""
        # ------------------------------
        grid = QGridLayout()
        grid.addWidget(label1, 0, 0)   # row 0, column 0
        grid.addWidget(label2, 0, 1)   # row 0, column 1
        grid.addWidget(label3, 0, 2)   # row 1, column 0
        grid.addWidget(label4, 1, 0)   # row 1, column 1
        grid.addWidget(label5, 1, 1)   # row 1, column 2

        # Apply chosen layout to central widget
        self.central_widget.setLayout(grid)


# -------- Entry Point --------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


# http://youtube.com/watch?v=ml-mBl77h6Q&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=81