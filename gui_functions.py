# Description: Funciones de la interfaz gráfica


def filtro_button_toggled(self, button, box):
    if button.isChecked():
        box.setEnabled(True)
        box.setCurrentIndex(0)
        if button == self.primerOrden_button:
            self.f0_label.setEnabled(True)
            self.f0_spinBox.setEnabled(True)
            self.f0_spinBox.setValue(0)
            self.f0_box.setEnabled(True)
            self.f0_box.setCurrentIndex(0)


        elif button == self.segundoOrden_button:
            self.w0_label.setEnabled(True)
            self.w0_spinBox.setEnabled(True)
            self.w0_spinBox.setValue(0)
            self.w0_box.setEnabled(True)

            self.xi_label.setEnabled(True)
            self.xi_spinBox.setEnabled(True)


    else:
        box.setEnabled(False)
        box.setCurrentIndex(-1)
        self.f0_label.setEnabled(False)
        self.f0_spinBox.setEnabled(False)
        self.f0_spinBox.setValue(0)
        self.f0_box.setEnabled(False)
        self.f0_box.setCurrentIndex(-1)
        self.w0_label.setEnabled(False)
        self.w0_spinBox.setEnabled(False)
        self.w0_spinBox.setValue(0)
        self.w0_box.setEnabled(False)
        self.xi_label.setEnabled(False)
        self.xi_spinBox.setEnabled(False)
        self.xi_spinBox.setValue(0)
    

def filtro_box_toggle(self, button, label1, label2 , text1, text2):
    if button.isChecked():
        label1.setEnabled(True)
        text1.setEnabled(True)

        label2.setEnabled(True)
        text2.setEnabled(True)

    else:
        label1.setEnabled(False)
        text1.setEnabled(False)

        label2.setEnabled(False)
        text2.setEnabled(False)

def fe_button_toggled(self):
    if self.feSenoide_button.isChecked():
        print("senoide")
        clear_fe(self)
        self.feAmplitud_label.setVisible(True)
        self.feAmplitud_text.setVisible(True)
        self.feAmplitud_text.setText("0")
        self.feAmplitud_box.setVisible(True)
        self.feAmplitud_box.setCurrentIndex(-1)

        self.feFrecuencia_label.setVisible(True)
        self.feFrecuencia_text.setVisible(True)
        self.feFrecuencia_text.setText("0")
        self.feFrecuencia_box.setVisible(True)
        self.feFrecuencia_box.setCurrentIndex(-1)



    elif self.feEscalon_button.isChecked():
        print("escalon")
        clear_fe(self)
        self.feAmplitud_label.setVisible(True)
        self.feAmplitud_text.setVisible(True)
        self.feAmplitud_text.setText("0")
        self.feAmplitud_box.setVisible(True)
        self.feAmplitud_box.setCurrentIndex(-1)
    
    elif self.fePulso_button.isChecked():
        print("pulso")
        clear_fe(self)
        self.feAmplitud_label.setVisible(True)
        self.feAmplitud_text.setVisible(True)
        self.feAmplitud_text.setText("0")
        self.feAmplitud_box.setVisible(True)
        self.feAmplitud_box.setCurrentIndex(-1)

        self.feFrecuencia_label.setVisible(True)
        self.feFrecuencia_text.setVisible(True)
        self.feFrecuencia_text.setText("0")
        self.feFrecuencia_box.setVisible(True)
        self.feFrecuencia_box.setCurrentIndex(-1)
    
def clear_fe(self):
        self.feAmplitud_label.setVisible(False)
        self.feAmplitud_text.setVisible(False)
        self.feAmplitud_text.setText("0")
        self.feAmplitud_box.setVisible(False)
        self.feAmplitud_box.setCurrentIndex(-1)

        self.feFrecuencia_label.setVisible(False)
        self.feFrecuencia_text.setVisible(False)
        self.feFrecuencia_text.setText("0")
        self.feFrecuencia_box.setVisible(False)
        self.feFrecuencia_box.setCurrentIndex(-1)
