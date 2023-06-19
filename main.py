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

        self.setWindowTitle("Simulador de filtros")
        self.setWindowIcon(QIcon("logo.png"))
        # self.setFixedSize(1200, 850)        

        self.show()

        self.connect_signals()




    def connect_signals(self):
        #Conecto los botones de la barra de filtros
        self.primerOrden_button.toggled.connect(lambda: gf.filtro_button_toggled(self, self.primerOrden_button, self.primerOrden_box))
        self.segundoOrden_button.toggled.connect(lambda: gf.filtro_button_toggled(self, self.segundoOrden_button, self.segundoOrden_box))
        self.ordenSuperior_button.toggled.connect(lambda: gf.filtro_box_toggle(self, self.ordenSuperior_button, self.numerador_label, self.denominador_label, self.numerador_text, self.denominador_text))

        #Conecto los botones de la barra de señales de entrada
        self.feSenoide_button.toggled.connect(lambda: gf.fe_button_toggled(self))
        self.feEscalon_button.toggled.connect(lambda: gf.fe_button_toggled(self))
        self.fePulso_button.toggled.connect(lambda: gf.fe_button_toggled(self))
        self.feTriangular_button.toggled.connect(lambda: gf.fe_button_toggled(self))
        self.feExponencial_button.toggled.connect(lambda: gf.fe_button_toggled(self))
        self.feImpulso_button.toggled.connect(lambda: gf.fe_button_toggled(self))

        #Conecto los botones de la barra de señales de salida
            #Tipo de señal
        self.feSenoide_button.toggled.connect(lambda: fplt.generate_input_signal(self))
        self.feEscalon_button.toggled.connect(lambda: fplt.generate_input_signal(self))
        self.fePulso_button.toggled.connect(lambda: fplt.generate_input_signal(self))
            #Tipo de filtro
        self.primerOrden_button.toggled.connect(lambda: fplt.generate_input_signal(self))
        self.segundoOrden_button.toggled.connect(lambda: fplt.generate_input_signal(self))
        self.ordenSuperior_button.toggled.connect(lambda: fplt.generate_input_signal(self))
            #Tipo de filtro de primer orden
        self.primerOrden_box.currentIndexChanged.connect(lambda: fplt.generate_input_signal(self))
            #Tipo de filtro de segundo orden
        self.segundoOrden_box.currentIndexChanged.connect(lambda: fplt.generate_input_signal(self))
            #Tipo de filtro de orden superior
        self.numerador_text.returnPressed.connect(lambda: fplt.generate_input_signal(self))
        self.denominador_text.returnPressed.connect(lambda: fplt.generate_input_signal(self))


            #Amplitud
        self.feAmplitud_text.valueChanged.connect(lambda: fplt.generate_input_signal(self))
            #Frecuencia
        self.feFrecuencia_text.valueChanged.connect(lambda: fplt.generate_input_signal(self))
            #Datos de filtro de primer orden
        self.f0_spinBox.valueChanged.connect(lambda: fplt.generate_input_signal(self))
        self.f0_box.currentIndexChanged.connect(lambda: fplt.generate_input_signal(self))
        self.ganancia_primerOrden_spinBox.valueChanged.connect(lambda: fplt.generate_input_signal(self))
            #Datos de filtro de segundo orden
        self.w0_spinBox.valueChanged.connect(lambda: fplt.generate_input_signal(self))
        self.w0_box.currentIndexChanged.connect(lambda: fplt.generate_input_signal(self))
        self.ganancia_segundoOrden_spinBox.valueChanged.connect(lambda: fplt.generate_input_signal(self))
        self.xi_spinBox.valueChanged.connect(lambda: fplt.generate_input_signal(self))
            #Escala entrada
        self.feAmplitud_box.currentIndexChanged.connect(lambda: fplt.generate_input_signal(self))
        self.feFrecuencia_box.currentIndexChanged.connect(lambda: fplt.generate_input_signal(self))
            



def main():
    app = QApplication([])
    window = gui()
    app.exec_()

if __name__ == "__main__":
    main()
