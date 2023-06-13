from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic


class gui(QMainWindow):
    def __init__(self):
        super(gui, self).__init__()
        uic.loadUi("gui.ui", self)
        self.show()

        #When the button is clicked, show me the combo box value
        self.radioButton.toggled.connect(self.on_radioButton_toggled)
        self.radioButton_2.toggled.connect(self.on_radioButton_2_toggled)


    def on_radioButton_toggled(self):
        if self.radioButton.isChecked():
            self.comboBox.setEnabled(True)
            self.comboBox.setCurrentIndex(0)
        else:
            self.comboBox.setEnabled(False)
            self.comboBox.setCurrentIndex(-1)

    def on_radioButton_2_toggled(self):
        if self.radioButton_2.isChecked():
            self.comboBox_2.setEnabled(True)
            self.comboBox_2.setCurrentIndex(0)
        else:
            self.comboBox_2.setEnabled(False)
            self.comboBox_2.setCurrentIndex(-1)
            



def main():
    app = QApplication([])
    window = gui()
    app.exec_()

if __name__ == "__main__":
    main()
