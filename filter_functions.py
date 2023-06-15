from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


# filtro de primer orden 
# pasa bajos separando el denomianador y numerador en dos listas con frecuencia variable
# y con variación de la ganancia del filtro
def fun_pb1(frec, fc, gan):
    num = [gan]
    dem = [1, fc]
    sys = signal.TransferFunction(num, dem)
    w, mag, phase = signal.bode(sys, frec)
    return w, mag, phase

# filtro de primer orden pasa altos con frecuencia variable
# y con variación de la ganancia del filtro
def fun_pa1(frec, fc, gan):
    num = [gan, 0]
    dem = [1, fc]
    sys = signal.TransferFunction(num, dem)
    w, mag, phase = signal.bode(sys, frec)
    return w, mag, phase

# filtro de primer orden pasa todo y ganancia
def fun_pt1(frec, gan):
    num = [gan]
    dem = [1]
    sys = signal.TransferFunction(num, dem)
    w, mag, phase = signal.bode(sys, frec)
    return w, mag, phase

# Filtro con polo y/o cero arbitrarios con control de frecuencia y ganancia
def fun_pcz(frec, gan, polos, ceros):
    num = [gan]
    dem = [1]
    for i in range(len(ceros)):
        num.append(-ceros[i])
    for i in range(len(polos)):
        dem.append(-polos[i])
    sys = signal.TransferFunction(num, dem)
    w, mag, phase = signal.bode(sys, frec)
    return w, mag, phase

# Filtros de segundo orden pasa bajos con coeficiente de amortiguamiento, wo y ganancia variables
def fun_pb2(frec, z, wo, gan):
    num = [gan*wo**2]
    dem = [1, 2*z*wo, wo**2]
    sys = signal.TransferFunction(num, dem)
    w, mag, phase = signal.bode(sys, frec)
    return w, mag, phase

# Filtros de segundo orden pasa altos con coeficiente de amortiguamiento, wo y ganancia variables
def fun_pa2(frec, z, wo, gan):
    num = [gan, 0, gan*wo**2]
    dem = [1, 2*z*wo, wo**2]
    sys = signal.TransferFunction(num, dem)
    w, mag, phase = signal.bode(sys, frec)
    return w, mag, phase

# Filtros de segundo orden pasa todo con coeficiente de amortiguamiento, wo y ganancia variables
def fun_pt2(frec, z, wo, gan):
    num = [gan*wo**2]
    dem = [1, 2*z*wo, wo**2]
    sys = signal.TransferFunction(num, dem)
    w, mag, phase = signal.bode(sys, frec)
    return w, mag, phase

# fitro de segundo orden pasa banda con coeficiente de amortiguamiento, wo y ganancia variables
def fun_pbanda2(frec, z, wo, gan):
    num = [gan*wo**2, 0, 0]
    dem = [1, 2*z*wo, wo**2]
    sys = signal.TransferFunction(num, dem)
    w, mag, phase = signal.bode(sys, frec)
    return w, mag, phase

# Filtro notch de segundo orden con w0, coef de amortiguamiento y ganancia variables
def fun_notch2(frec, z, wo, gan):
    num = [gan * (wo**2), 0, gan]
    dem = [wo**2 , 2*z*wo, ]
    sys = signal.TransferFunction(num, dem)
    w, mag, phase = signal.bode(sys, frec)
    return w, mag, phase

# Filtro low pass notch de segundo orden con coeficiente de amoritguamiento, wo y ganancia variables
def fun_lpn2(frec, z, wo, gan):
    num = [gan*wo**2, 0, gan*wo**2]
    dem = [1, 2*z*wo, wo**2]
    sys = signal.TransferFunction(num, dem)
    w, mag, phase = signal.bode(sys, frec)
    return w, mag, phase

# Filtro high pass notch de segundo orden con coeficiente de amoritguamiento, wo y ganancia variables
def fun_hpn2(frec, z, wo, gan):
    num = [gan, 0, gan]
    dem = [1, 2*z*wo, wo**2]
    sys = signal.TransferFunction(num, dem)
    w, mag, phase = signal.bode(sys, frec)
    return w, mag, phase

# Filtro de segundo orden con polos y/o ceros arbitrarios
def fun_pcz2(frec, gan, polos, ceros):
    num = [gan]
    dem = [1]
    for i in range(len(ceros)):
        num.append(-ceros[i])
    for i in range(len(polos)):
        dem.append(-polos[i])
    sys = signal.TransferFunction(num, dem)
    w, mag, phase = signal.bode(sys, frec)
    return w, mag, phase

# Filtros de orden superior
def fun_pczn(frec, gan, polos, ceros):
    num = [gan]
    dem = [1]
    for i in range(len(ceros)):
        num.append(-ceros[i])
    for i in range(len(polos)):
        dem.append(-polos[i])
    sys = signal.TransferFunction(num, dem)
    w, mag, phase = signal.bode(sys, frec)
    return w, mag, phase


