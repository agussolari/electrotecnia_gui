import input_signals as isig
import matplotlib.pyplot as plt

input_signal = isig.input_signal()

# def update_input_plot(self):
#     self.MplWidget.canvas.axes.clear()
#     self.MplWidget.canvas.axes.plot(input_signal.tt, input_signal.st)
#     self.MplWidget.canvas.axes.legend(('test1', 'test2'))
#     self.MplWidget.canvas.draw()

def generate_input_signal(self):
    print("Generating input signal")
    if self.feSenoide_button.isChecked():

        a0 = self.feAmplitud_text.text()
        f0 = self.feFrecuencia_text.text()

        if a0 != '' and f0 != '' and float(a0) > 0 and float(f0) > 0:
            # self.update_input_plot(self)
            input_signal = isig.generate_sinusoidal_signal(100, float(f0), 1, float(a0), 0)
            #plot input signal with matplotlib
            plt.plot(input_signal)
            plt.show()













            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(isig.generate_sinusoidal_signal(100, float(f0), 1, float(a0), 0))
            self.MplWidget.canvas.axes.legend(('test1', 'test2'))
            self.MplWidget.canvas.draw()


    elif self.feEscalon_button.isChecked():
            print("Escalon")
    elif self.fePulso_button.isChecked():
            print("Pulso")

