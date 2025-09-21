import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("PyQt5 CheckBox Example")

        # Create a checkbox
        self.checkbox = QCheckBox("Do you like food?", self)
        self.initUI()

    def initUI(self):
        # --- Checkbox Setup ---
        self.checkbox.setGeometry(10, 0, 500, 100)   # x, y, width, height
        self.checkbox.setStyleSheet(
            "font-size: 50px;"
            "font-family: Arial;"
        )

        # "stateChanged" is a SIGNAL that fires whenever the checkbox is toggled
        # We connect it to our SLOT (checkbox_changed method)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    # SLOT (Triggered when checkbox changes)
    def checkbox_changed(self):
        if self.checkbox.isChecked():   
            print("You like food")
        else:
            print("You DO NOT like food")
    

    {"""
    def checkbox_changed(self, state):
        if state == Qt.Checked:         # Qt.Checked == 2
            print("You like food")
        elif state == Qt.Unchecked:     # Qt.Unchecked == 0
            print("You DO NOT like food")
     
        # (Optional) Qt.PartiallyChecked == 1 if tristate checkboxes are enabled
        # Use stateChanged with state values when you want tristate checkboxes or need to know the exact state. 
    """}


# Entry Point
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


# https://www.youtube.com/watch?v=VgnUB_vzR9I&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=85