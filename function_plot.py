import input_signals as isig
import matplotlib.pyplot as plt
import numpy as np
import output_signals as osig

def generate_input_signal(self):
    #obtengo los escalamientoa
    Ascale = self.feAmplitud_box.currentIndex()
    Fscale = self.feFrecuencia_box.currentIndex()
    #si las cajas estan vacías, por default grafica en V y Hz
    if Ascale < 0:
        Ascale = 2
    if Fscale < 0:
        Fscale = 0

    self.MplWidget.canvas.axes.clear()

    if self.feSenoide_button.isChecked():
        a0 = self.feAmplitud_text.value() * (10 ** (3*Ascale-6))
        f0 = self.feFrecuencia_text.value() * (10 ** (3*Fscale))
        
        if a0 !=0 and f0 !=0:
            isig.input_signal.tt, isig.input_signal.st = isig.generate_sinusoidal_signal(100, float(f0), 10000, float(a0), 0)
            self.MplWidget.canvas.axes.plot(isig.input_signal.tt, isig.input_signal.st)
            osig.test(self)

    elif self.feEscalon_button.isChecked():
        a0 = self.feAmplitud_text.value() * (10 ** (3*Ascale-6))

        if a0 !=0:
            isig.input_signal.tt, isig.input_signal.st = isig.generate_step_signal(100, 100, float(a0))
            self.MplWidget.canvas.axes.plot(isig.input_signal.tt, isig.input_signal.st)
            osig.test(self)

    elif self.fePulso_button.isChecked():
        a0 = self.feAmplitud_text.value() * (10 ** (3*Ascale-6))
        f0 = self.feFrecuencia_text.value() * (10 ** (3*Fscale))

        if a0 !=0  and f0 !=0:
            isig.input_signal.tt, isig.input_signal.st = isig.generate_square_signal(100, float(f0), 100, float(a0), 0, 0.5)
            self.MplWidget.canvas.axes.plot(isig.input_signal.tt, isig.input_signal.st)
            osig.test(self)

    elif self.feTriangular_button.isChecked():
        a0 = self.feAmplitud_text.value() * (10 ** (3*Ascale-6))
        f0 = self.feFrecuencia_text.value() * (10 ** (3*Fscale))

        if a0 !=0  and f0 !=0:
            isig.input_signal.tt, isig.input_signal.st = isig.generate_triangular_signal(100, float(f0), 100, float(a0), 0, 0.5)
            self.MplWidget.canvas.axes.plot(isig.input_signal.tt, isig.input_signal.st)
            osig.test(self)
            
    elif self.feExponencial_button.isChecked():
        a0 = self.feAmplitud_text.value() * (10 ** (3*Ascale-6))
        f0 = self.feFrecuencia_text.value() * (10 ** (3*Fscale))

        if a0 !=0  and f0 !=0:
            isig.input_signal.tt, isig.input_signal.st = isig.generate_exponential_signal(100, float(f0), 100, float(a0), 0, 0.5)
            self.MplWidget.canvas.axes.plot(isig.input_signal.tt, isig.input_signal.st)
            osig.test(self)

    elif self.feImpulso_button.isChecked():
        a0 = self.feAmplitud_text.value() * (10 ** (3*Ascale-6))

        if a0 !=0:
            isig.input_signal.tt, isig.input_signal.st = isig.generate_impulse_signal(100, 100, float(a0))
            self.MplWidget.canvas.axes.plot(isig.input_signal.tt, isig.input_signal.st)
            osig.test(self)
            
    self.MplWidget.canvas.axes.legend("E", loc='lower left', shadow=True, fontsize='small', frameon=False)

    self.MplWidget.canvas.axes.set_xlabel("Tiempo [s]")
    self.MplWidget.canvas.axes.set_ylabel("Tensión [V]")
    self.MplWidget.canvas.axes.grid(True)
    self.MplWidget.figure.tight_layout()
    self.MplWidget.canvas.draw()