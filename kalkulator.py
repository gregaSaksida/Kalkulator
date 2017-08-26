import math

class Vektor:
    
    def __init__(self, vektor = [0, 0, 0]):
        self.vektor = list(vektor)
        self.razseznost = len(self.vektor)
        self.je_vektor = None
    
    
    def __add__(self, drugi):
        try:
            drugi.je_vektor
        except AttributeError:
            print('Seštevanja ni mogoče izvesti.'
                  ' Eden od operandov ni niti vektor niti skalar.')
            return None
        
        else:
            if self.razseznost != drugi.razseznost:
                print('Seštevanja ni mogoče izvesti.'
                  ' Vektorja nimata enakega števila komponent.')
                return None
            vsota = []
            for i, komponenta in enumerate(self.vektor):
                vsota.append(komponenta + drugi.vektor[i])
            return Vektor(vsota)
        
    
    def __mul__(self, drugi):
        
        try:
            drugi.je_vektor
        except AttributeError:
            pass
        else:
            if self.razseznost != drugi.razseznost:
                print('Množenja ni mogoče izvesti.'
                      ' Vektorja nimata enakega števila komponent.')
                return None
            produkt = 0
            for i, komponenta in enumerate(self.vektor):
                produkt += komponenta * drugi.vektor[i]
            return produkt
        
        try:
            drugi + 0
        except TypeError or AttributeError:
            print('Množenja ni mogoče izvesti.'
                  ' Eden od operandov ni niti vektor niti skalar.')
            return None
        else:
            nov_vektor = []
            for i in range(self.razseznost):
                nov_vektor.append(drugi * self.vektor[i])
            return Vektor(nov_vektor)
        
    
    def __sub__(self, drugi):
        return self + (-1 * drugi)
    
    def __radd__(self, napacen):
        return self + napacen

    def __rmul__(self, skalar):
        return self * skalar
    
    def __rsub__(self, napacen):
        return self - napacen
        
    
    def __repr__(self):
        return 'Vektor({0})'.format(self.vektor)
    
    def __str__(self):
        return '{0}'.format(tuple(self.vektor))


def Dolzina(vektor):
    dolzina = 0
    for komponenta in vektor.vektor:
        dolzina += komponenta ** 2
    return dolzina ** (1 / 2)

def cos_kota(vektor1, vektor2):
    print(vektor1 * vektor2)
    return (vektor1 * vektor2) / (Dolzina(vektor1) * Dolzina(vektor2))

def kot(vektor1, vektor2):
    return math.arccos(cos_kota(vektor1, vektor2))
    
    
class Matrika:
    
    def __init__(self, matrika = [[0, 0], [0, 0]]):
        self.matrika = list(matrika)
        self.m = len(self.matrika)
        for i in range(self.m):
            self.matrika[i] = list(self.matrika[i])
        self.n = len(self.matrika[0])
    
    def __repr__(self):
        return 'Matrika({0})'.format(self.matrika)
    
    def __str__(self):
        if self.m < 20 and self.n < 20:
            for vrstica in self.matrika:
                print(vrstica)
        else:
            print(self.matrika)
        return '\n{0}x{1} razsežna matrika.'.format(self.m, self.n)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    