from scipy import signal

class FilterFirstOrder:
    def __init__(self, frecuencia, ganancia):
        self.frec = frecuencia
        self.gan = ganancia

    def fun_pb1(self):
        num = [self.gan]
        den = [1/self.frec, 1]
        sys = signal.TransferFunction(num, den)
        w, mag, phase = signal.bode(sys, self.frec)
        return w, mag, phase, num, den

    def fun_pa1(self):
        num = [self.gan, 0]
        den = [1/self.frec, 1]
        sys = signal.TransferFunction(num, den)
        w, mag, phase = signal.bode(sys, self.frec)
        return w, mag, phase, num, den

    def fun_pt1(self):
        num = [self.gan/self.frec, -self.gan]
        den = [1/self.frec, 1]
        sys = signal.TransferFunction(num, den)
        w, mag, phase = signal.bode(sys, self.frec)
        return w, mag, phase, num, den

    

class FilterSecondOrder:
    def __init__(self, frecuencia, ganancia, epsilon):
        self.wo = frecuencia
        self.gan = ganancia
        self.z = epsilon

    def fun_pb2(self):
        num = [self.gan]
        den = [(1/(self.wo**2)), (2*self.z/self.wo), 1]
        sys = signal.TransferFunction(num, den)
        w, mag, phase = signal.bode(sys, self.wo)
        return w, mag, phase, num, den

    def fun_pa2(self):
        num = [self.gan,0,0]
        den = [(1/(self.wo**2)), (2*self.z/self.wo), 1]
        sys = signal.TransferFunction(num, den)
        w, mag, phase = signal.bode(sys, self.wo)
        return w, mag, phase, num, den

    def fun_pt2(self):
        num = [(self.gan/(self.wo**2)),(-2*self.z/self.wo),1]
        den = [(1/(self.wo**2)), (2*self.z/self.wo), 1]
        sys = signal.TransferFunction(num, den)
        w, mag, phase = signal.bode(sys, self.wo)
        return w, mag, phase, num, den

    def fun_pbanda2(self):
        num = [0, self.gan, 0]
        den = [(1/(self.wo**2)), (2*self.z/self.wo),1]
        sys = signal.TransferFunction(num, den)
        w, mag, phase = signal.bode(sys, self.wo)
        return w, mag, phase, num, den




class FilterNotch:
    def __init__(self, frecPolo, frecCero, ganancia, epsilonPolo, epsilonCero):
        self.wp = frecPolo
        self.wc = frecCero
        self.gan = ganancia
        self.zp = epsilonPolo
        self.zc = epsilonCero

    #https://www.electrical4u.com/band-stop-notch-filter/
    def fun_notchbase(self):
        num = [self.gan, 0, self.gan/(self.wc**2)]
        den = [1 , self.zp*self.wp, (self.wp**2)]
        sys = signal.TransferFunction(num, den)
        w, mag, phase = signal.bode(sys)
        return w, mag, phase, num, den
    #wp = wc -> notch estandar
    #wp < wc -> low pass
    #wp > wc -> high pass

    
    def fun_notch(self):
        num = [(self.gan*(1/(self.wp**2))), 0, self.gan]
        den = [(1/(self.wp**2)) , 2*self.zp*(1/(self.wp)), 1]
        sys = signal.TransferFunction(num, den)
        w, mag, phase = signal.bode(sys, self.wp)
        return w, mag, phase, num, den

    def fun_lpn(self):
        num = [(self.gan*(1/(self.wc**2))), 2*self.gan*self.zc*(1/(self.wc)), self.gan]
        den = [(1/(self.wp**2)) , 2*self.zp*(1/(self.wp)), 1]
        sys = signal.TransferFunction(num, den)
        w, mag, phase = signal.bode(sys)
        return w, mag, phase, num, den
    
    def fun_hpn(self):
        num = [(self.gan*(1/(self.wc**2))), 2*self.gan*self.zc*(1/self.wc), self.gan]
        den = [(1/self.wp**2) , 2*self.zp*(1/self.wp), 1]
        sys = signal.TransferFunction(num, den)
        w, mag, phase = signal.bode(sys)
        return w, mag, phase, num, den


class FilterConfig:
    def __init__(self, ganancia, polos, ceros):
        self.gan = ganancia
        self.polos = polos
        self.ceros = ceros

    def fun_config(self):
        num = [self.gan]
        den = [1]
        for i in range(len(self.ceros)):
            num.append(-self.ceros[i])
        for i in range(len(self.polos)):
            den.append(-self.polos[i])
        sys = signal.TransferFunction(num, den)
        w, mag, phase = signal.bode(sys)
        return w, mag, phase, num, den