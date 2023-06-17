import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import math
import mplwidget as mpl

from sympy.integrals.transforms import laplace_transform
from sympy.integrals.transforms import inverse_laplace_transform
from sympy.abc import s, t

import input_signals as isig
from scipy import signal
from sympy import symbols, inverse_laplace_transform
import numpy as np


def test(self):
    """
    #input_transform = laplace_transform(isig.input_signal.st, isig.input_signal.tt , s)
    #print(input_transform)
    
    #Definir la función de transferencia en términos de 's'

    funcion_transferencia = signal.TransferFunction([3], [1, 2*(0.5)*1000, 1000**2])  # Ejemplo de función de transferencia
    print(funcion_transferencia)


    #Obtener la respuesta al impulso en el dominio del tiempo
    t, h = signal.impulse(funcion_transferencia)

    # Datos de entrada
    x = isig.input_signal.tt  # Vector de tiempo original
    y = isig.input_signal.st  # Valores de la señal original en esos momentos

    # Interpolar los valores de la señal original en el dominio del tiempo de la respuesta al impulso
    y_interpolada = np.interp(t, x, y)

    salida = y_interpolada * h
    

    self.mpl.MplWidget.canvas.axes.clear()
    self.mpl.MplWidget.canvas.axes.plot(t, salida)
    self.mpl.MplWidget.canvas.axes.legend(('test1', 'test2'))
    self.mpl.MplWidget.canvas.draw()
    """
#transformar una señal mediante la transformada de laplace a partir de los puntos en x e y de la señal


    # Datos de entrada
    tiempo_entrada = isig.input_signal.tt  # Vector de tiempo de la entrada
    valores_entrada = isig.input_signal.st  # Valores de la entrada en esos momentos
    numerador = [3]  # Numerador de la función de transferencia
    denominador = [1, 2*(0.5)*1000, 1000**2]  # Denominador de la función de transferencia

    # Realizar la transformada de Laplace de la entrada
    s = symbols('s')
    print("test")
    entrada_transformada = laplace_transform(valores_entrada, tiempo_entrada)
    print("test2")
    print(entrada_transformada)
    # Multiplicar la transformada de Laplace de la entrada por la función de transferencia
    salida_transformada = signal.TransferFunction(numerador, denominador) * entrada_transformada

    # Realizar la antitransformación de Laplace y obtener la salida en el dominio del tiempo
    t = symbols('t')
    salida_tiempo = inverse_laplace_transform(salida_transformada, s, t)

    print("Salida en el dominio del tiempo:")
    print(salida_tiempo)
    # plt.plot(t, salida_tiempo)
    # plt.show()


