import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy as np

import input_signals as isig
import mplwidget as mpl

from scipy import signal


def test(self):
    # Datos de entrada
    tiempo_entrada = isig.input_signal.tt  # Vector de tiempo de la entrada
    valores_entrada = isig.input_signal.st  # Valores de la entrada en esos momentos

    #Función de transferencia
    numerador = [3]  # Numerador de la función de transferencia
    denominador = [1, 2*(0.5)*1, 1**2]  # Denominador de la función de transferencia

    # Salida del sistema
    lti = signal.lti(numerador, denominador)  # Creo el sistema
    tiempo_salida, salida, x = signal.lsim(lti, valores_entrada, tiempo_entrada)  # Obtengo la salida del sistema

    print("Ploting output signal")
    # Grafico la salida
    self.MplWidget.canvas.axes.plot(tiempo_salida, salida)
    self.MplWidget.canvas.axes.legend("Salida")
    self.MplWidget.canvas.draw()

