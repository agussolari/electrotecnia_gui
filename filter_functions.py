from scipy import signal
import numpy as np
import sympy

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
        den = [1, self.frec]
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
    def __init__(self, frecuencia, ganancia, xi, gan_banda_pasante):
        self.wo = frecuencia
        self.gan = ganancia
        self.z = xi
        self.gan_banda_pasante = gan_banda_pasante

    def fun_pb2(self):
        if(self.gan_banda_pasante):
            self.gan = 2 * self.z * self.gan
        num = [self.gan]
        den = [(1/(self.wo**2)), (2*self.z/self.wo), 1]
        sys = signal.TransferFunction(num, den)
        w, mag, phase = signal.bode(sys, self.wo)
        return w, mag, phase, num, den

    def fun_pa2(self):
        if(self.gan_banda_pasante):
            self.gan = 2 * self.z * self.gan
        num = [self.gan,0,0]
        den = [1, (2*self.z*self.wo), (self.wo**2)]
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
        num = [0, (self.gan*2*self.z)/(self.wo), 0]
        den = [(1/(self.wo**2)), (2*self.z/self.wo),1]
        sys = signal.TransferFunction(num, den)
        w, mag, phase = signal.bode(sys, self.wo)
        return w, mag, phase, num, den

    def fun_notch(self):
        num = [(self.gan*(1/(self.wo**2))), 0, self.gan]
        den = [(1/(self.wo**2)) , 2*self.z*(1/(self.wo)), 1]
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
    def __init__(self, ganancia, polos_str, ceros_str):  # "1,4,3.5,8-3j"
        self.gan = ganancia
        self.polos = polos_str.split(",")
        self.ceros = ceros_str.split(",")

    def fun_config(self):
        num = (self.gan * np.polynomial.polynomial.polyfromroots(self.ceros))
        den = np.polynomial.polynomial.polyfromroots(self.polos)
        sys = signal.TransferFunction(num, den)
        w, mag, phase = signal.bode(sys)
        return w, mag, phase, num, den



def get_poly_coeffs(poly_str):
    # Convert the string to a Sympy expression
    x = sympy.symbols('x')
    poly_expr = sympy.sympify(poly_str)

    # Get the coefficients of the polynomial
    coeffs = sympy.Poly(poly_expr, x).all_coeffs()

    return coeffs

    
class FilterCustom:
    def __init__(self, num_str , den_str):
        self.num = []
        self.den = []
        if num_str != "" and den_str != "":
            self.num = get_poly_coeffs(num_str)
            self.den = get_poly_coeffs(den_str)

            

    def fun_custom(self):
        if (self.num != [] and self.den != []) or (self.num != None and self.den != None):
            if(len(self.den)>=len(self.num)):

            
                num_float = list(map(float, self.num))
                den_float = list(map(float, self.den))
            
                sys = signal.TransferFunction(num_float, den_float)
                w, mag, phase = signal.bode(sys)
                return w, mag, phase, num_float, den_float

