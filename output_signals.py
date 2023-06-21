import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy as np
import sys

import input_signals as isig
import mplwidget as mpl
import filter_functions as ff

from scipy import signal
from enum import Enum


class primerOrden_filtros(Enum):
    P_PASABAJOS = 0
    P_PASAALTOS = 1
    P_PASATODO = 2

class segundoOrden_filtros(Enum):
    S_PASABAJOS = 0
    S_PASAALTOS = 1
    S_PASATODO = 2
    S_PASABANDA = 3
    S_NOTCH = 4

class salida:
    def __init__(self, w0 = None , mag = None, phase = None, num = None, den = None):
        self.w = w0
        self.mag = mag
        self.phase = phase
        self.num = num
        self.den = den

        





def processEntry(self):
    # Datos de entrada
    tiempo_entrada = isig.input_signal.tt  # Vector de tiempo de la entrada
    valores_entrada = isig.input_signal.st  # Valores de la entrada en esos momentos

    # Datos de salida
    w0 = 0
    mag = 0
    phase = 0

    numerador_transferencia = []
    denominador_transferencia = []


    fn_salida = salida()
    #obtengo los escalamientos
    Wscale = self.w0_box.currentIndex()
    Fscale = self.f0_box.currentIndex()
    #si las cajas estan vacías, por default grafica en Hz y rad/seg
    if Wscale < 0:
        Wscale = 0
    if Fscale < 0:
        Fscale = 0


    #Obtengo el tipo de filtro de primer orden
    if self.primerOrden_button.isChecked():

        ganancia = float(self.ganancia_primerOrden_spinBox.value())
        if (self.primerOrden_Db_button.isChecked()):
            ganancia =  10**(ganancia/20)
        
        frecuencia = float(self.f0_spinBox.value()) * (10 ** (3*Fscale))

        primerOrden_index =  self.primerOrden_box.currentIndex()

        if frecuencia != 0 and ganancia != 0:
            primerOrden_filter = ff.FilterFirstOrder(frecuencia, ganancia)

            if primerOrden_index == primerOrden_filtros.P_PASABAJOS.value:
                w0, mag, phase, numerador_transferencia, denominador_transferencia = primerOrden_filter.fun_pb1()

            
            elif primerOrden_index == primerOrden_filtros.P_PASAALTOS.value:
                w0, mag, phase, numerador_transferencia, denominador_transferencia = primerOrden_filter.fun_pa1()

            elif primerOrden_index == primerOrden_filtros.P_PASATODO.value:
                w0, mag, phase, numerador_transferencia, denominador_transferencia = primerOrden_filter.fun_pt1()


    #Obtengo el tipo de filtro de segundo orden
    elif self.segundoOrden_button.isChecked():
        
        ganancia = float(self.ganancia_segundoOrden_spinBox.value())
        
        if self.segundoOrden_Db_button.isChecked():
            ganancia = 10**(ganancia/20) 

        w0 = float(self.w0_spinBox.value()) * (10 ** (3*Wscale))
        xi = float(self.xi_spinBox.value())

        ganancia_banda_pasante = 0
        if(self.gananciaMaxima_button.isChecked()):
            ganancia_banda_pasante = 1


        segundoOrden_index = self.segundoOrden_box.currentIndex()

        if w0 != 0 and ganancia != 0 and xi != 0:
            segundoOrden_filter = ff.FilterSecondOrder(w0, ganancia, xi, ganancia_banda_pasante)

            if segundoOrden_index == segundoOrden_filtros.S_PASABAJOS.value:
                w0, mag, phase, numerador_transferencia, denominador_transferencia = segundoOrden_filter.fun_pb2()
            
            elif segundoOrden_index == segundoOrden_filtros.S_PASAALTOS.value:
                w0, mag, phase, numerador_transferencia, denominador_transferencia = segundoOrden_filter.fun_pa2()
            
            elif segundoOrden_index == segundoOrden_filtros.S_PASATODO.value:
                w0, mag, phase, numerador_transferencia, denominador_transferencia = segundoOrden_filter.fun_pt2()
            
            elif segundoOrden_index == segundoOrden_filtros.S_PASABANDA.value:
                w0, mag, phase, numerador_transferencia, denominador_transferencia = segundoOrden_filter.fun_pbanda2()

            elif segundoOrden_index == segundoOrden_filtros.S_NOTCH.value:
                w0, mag, phase, numerador_transferencia, denominador_transferencia = segundoOrden_filter.fun_notch()
            

    #Obtengo el tipo de filtro de orden superior
    elif self.ordenSuperior_button.isChecked():
        num_string = self.numerador_text.text()
        den_string = self.denominador_text.text()

        if num_string != "" and den_string != "" and num_string != None and den_string != None:
            ordenSuperior_filter = ff.FilterCustom(num_string, den_string)
            w0, mag, phase, numerador_transferencia, denominador_transferencia = ordenSuperior_filter.fun_custom()
            

            


    # Obtengo la transferencia del sistema
    # Salida del sistema
    if self.primerOrden_button.isChecked() or self.segundoOrden_button.isChecked() or self.ordenSuperior_button.isChecked() :
        if numerador_transferencia != [] and denominador_transferencia != [] and valores_entrada != [] and tiempo_entrada != []:
            lti = signal.lti(numerador_transferencia, denominador_transferencia)  # Creo el sistema
            tiempo_salida, datos_salida, x = signal.lsim(lti, valores_entrada, tiempo_entrada)  # Obtengo la salida del sistema

            # Grafico la salida
            self.MplWidget.canvas.axes.plot(tiempo_salida, datos_salida, color = "orange", label="Salida")
            self.MplWidget.canvas.axes.set_xlabel('Tiempo [s]')
            self.MplWidget.canvas.draw()

            #Grafico 
            #Clear
            w, m, p = signal.TransferFunction(numerador_transferencia, denominador_transferencia).bode()

            self.MplWidget_2.canvas.axes.clear()
            self.MplWidget_2.canvas.axes.semilogx(w, m, color = "blue", scalex = True)
            self.MplWidget_2.canvas.axes.set_xscale("log")
            self.MplWidget_2.canvas.axes.set_yscale("linear")
            self.MplWidget_2.canvas.axes.set_xlabel('Frecuencia [Hz]')
            self.MplWidget_2.canvas.axes.set_ylabel('Amplitud [dB]')
            self.MplWidget_2.canvas.axes.grid(True, which="both")
            self.MplWidget_2.figure.tight_layout()
            self.MplWidget_2.canvas.draw()
            
            self.MplWidget_3.canvas.axes.clear()
            self.MplWidget_3.canvas.axes.semilogx(w,p)
            self.MplWidget_3.canvas.axes.set_xscale("log")
            self.MplWidget_3.canvas.axes.set_yscale("linear")
            self.MplWidget_3.canvas.axes.set_xlabel('Frecuencia [Hz]')
            self.MplWidget_3.canvas.axes.set_ylabel('Fase [°]')
            self.MplWidget_3.canvas.axes.grid(True, which="both")
            self.MplWidget_3.figure.tight_layout()
            self.MplWidget_3.canvas.draw()
            
            self.MplWidget_4.canvas.axes.clear()
            self.MplWidget_4.canvas.axes.scatter(lti.zeros.real, lti.zeros.imag, marker = 'o', color = 'blue', label = 'Ceros', s=100)
            self.MplWidget_4.canvas.axes.scatter(lti.poles.real, lti.poles.imag, marker = 'x', color = 'red', label = 'Polos', s=100)
            self.MplWidget_4.canvas.axes.axhline(0, color='black', linewidth=1)
            self.MplWidget_4.canvas.axes.axvline(0, color='black', linewidth=1)
            self.MplWidget_4.canvas.axes.set_xlabel('σ')
            self.MplWidget_4.canvas.axes.set_ylabel('jω')
            self.MplWidget_4.canvas.axes.grid(True, which="both")
            self.MplWidget_4.figure.tight_layout()
            self.MplWidget_4.canvas.draw()



        

