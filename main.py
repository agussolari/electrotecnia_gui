from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)


import gui_functions as gf
import mplwidget as mpl
import input_signals as isig
import function_plot as fplt



app: QApplication = QApplication([])  # Start the application
print("Application started")


class gui(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui.ui", self)
        self.show()

        self.connect_signals()




    def connect_signals(self):
        #When the button is clicked, show me the combo box value
        self.primerOrden_button.toggled.connect(lambda: gf.filtro_button_toggled(self, self.primerOrden_button, self.primerOrden_box))
        self.segundoOrden_button.toggled.connect(lambda: gf.filtro_button_toggled(self, self.segundoOrden_button, self.segundoOrden_box))
        self.ordenSuperior_button.toggled.connect(lambda: gf.filtro_box_toggle(self, self.ordenSuperior_button, self.numerador_label, self.denominador_label, self.numerador_text, self.denominador_text))

        self.feSenoide_button.toggled.connect(lambda: gf.fe_button_toggled(self))
        self.feEscalon_button.toggled.connect(lambda: gf.fe_button_toggled(self))
        self.fePulso_button.toggled.connect(lambda: gf.fe_button_toggled(self))

        self.feSenoide_button.toggled.connect(lambda: fplt.generate_input_signal(self))
        self.feEscalon_button.toggled.connect(lambda: fplt.generate_input_signal(self))
        self.fePulso_button.toggled.connect(lambda: fplt.generate_input_signal(self))

        self.feAmplitud_text.textChanged.connect(lambda: fplt.generate_input_signal(self))
        self.feFrecuencia_text.textChanged.connect(lambda: fplt.generate_input_signal(self))

            



def main():
    app = QApplication([])
    window = gui()
    app.exec_()

if __name__ == "__main__":
    main()
