import input_signals as isig
import matplotlib.pyplot as plt
import numpy as np

input_signal = isig.input_signal()


def generate_input_signal(self):
    print("Generating input signal")

    if self.feSenoide_button.isChecked():
        a0 = self.feAmplitud_text.text()
        f0 = self.feFrecuencia_text.text()

        if a0 != '' and f0 != '' and float(a0) > 0 and float(f0) > 0:
            # self.update_input_plot(self)
            input_signal = isig.generate_sinusoidal_signal(100, float(f0), 100, float(a0), 0)
            #plot input signal with matplotlib
            print("Plotting input signal")
            tt, st = input_signal

            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(tt, st)
            self.MplWidget.canvas.axes.legend(('test1', 'test2'))
            self.MplWidget.canvas.draw()

        else:
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.draw()



    elif self.feEscalon_button.isChecked():
        a0 = self.feAmplitud_text.text()

        if a0 != '' and float(a0) > 0:
            # self.update_input_plot(self)
            input_signal = isig.generate_step_signal(100, 100, float(a0))
            #plot input signal with matplotlib
            print("Plotting input signal")
            tt, st = input_signal


            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(tt, st)
            self.MplWidget.canvas.axes.legend(('test1', 'test2'))
            self.MplWidget.canvas.draw()
        else:
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.draw()


    elif self.fePulso_button.isChecked():

        a0 = self.feAmplitud_text.text()
        f0 = self.feFrecuencia_text.text()

        if a0 != '' and f0 != '' and float(a0) > 0 and float(f0) > 0:
            # self.update_input_plot(self)
            input_signal = isig.generate_square_signal(100, float(f0), 100, float(a0), 0, 0.5)
            #plot input signal with matplotlib
            print("Plotting input signal")
            tt, st = input_signal

            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(tt, st)
            self.MplWidget.canvas.axes.legend(('test1', 'test2'))
            self.MplWidget.canvas.draw()

        else:
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.draw()

