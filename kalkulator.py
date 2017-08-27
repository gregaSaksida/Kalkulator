"""Ne pozabi:
    vektorski produkt
    transponiranje
    determinante
    lastne vrednosti, vektorji
    
    vektor ne sme biti 'nested list'
"""

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
                  ' Eden od operandov ni vektor.')
            return None
        
        else:
            if self.razseznost != drugi.razseznost:
                print('Seštevanja ni mogoče izvesti.'
                  ' Vektorja nista enako razsežna.')
                return None
            nov_vektor = []
            for i, komponenta in enumerate(self.vektor):
                nov_vektor.append(komponenta + drugi.vektor[i])
            return Vektor(nov_vektor)
        
    
    def __mul__(self, drugi):
        
        try:
            drugi.je_vektor
        except AttributeError:
            pass
        else:
            if self.razseznost != drugi.razseznost:
                print('Množenja ni mogoče izvesti.'
                      ' Vektorja nista enako razsežna.')
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


def dolzina(vektor):
    dolzina_ = 0
    for komponenta in vektor.vektor:
        dolzina_ += komponenta ** 2
    return dolzina_ ** (1 / 2)

def cos_kota(vektor1, vektor2):
    print(vektor1 * vektor2)
    return (vektor1 * vektor2) / (dolzina(vektor1) * dolzina(vektor2))

def kot(vektor1, vektor2):
    return math.arccos(cos_kota(vektor1, vektor2))
    
    
class Matrika:
    
    def __init__(self, matrika = [[0, 0], [0, 0]]):
        self.matrika = list(matrika)
        self.m = len(self.matrika)
        for i in range(self.m):
            self.matrika[i] = list(self.matrika[i])
        self.n = len(self.matrika[0])
        self.je_matrika = None
    
    def __repr__(self):
        return 'Matrika({0})'.format(self.matrika)
    
    def __str__(self):
        if self.m < 20 and self.n < 20:
            for vrstica in self.matrika:
                print(vrstica)
        else:
            print(self.matrika)
        return '\n{0}x{1} razsežna matrika.'.format(self.m, self.n)
    
    def transponirana(self):
        stolpci = []
        for n in range(self.n):
            stolpci.append([vrstica[n] for vrstica in self.matrika])
        self.matrika = stolpci
        stevilo_stolpcev = self.m
        self.m = self.n
        self.n = stevilo_stolpcev
    

def transponiranje(matrika):
    nova_matrika = Matrika(matrika.matrika)
    nova_matrika.transponirana()
    return nova_matrika
    

class Matrika(Matrika):
    
    def __add__(self, druga):
        try:
            druga.je_matrika
        except AttributeError:
            print('Seštevanja ni mogoče izvesti.'
                  ' Eden od operandov ni matrika.')
            return None
        
        else:
            if self.n != druga.n or self.m != druga.m:
                print('Seštevanja ni mogoče izvesti.'
                  ' Matriki nista enako veliki.')
                return None
            nova_matrika = []
            for m in range(self.m):
                vrstica = []
                for n in range(self.n):
                    vrstica.append(self.matrika[m][n] + druga.matrika[m][n])
                nova_matrika.append(vrstica)
            return Matrika(nova_matrika)
    
    
    def __mul__(self, druga):
        try:
            druga.je_matrika
        except AttributeError:
            pass
        
        else:
            if self.n != druga.m:
                print('Število stolpcev prve matrike ni enako številu'
                      ' vrstic druge matrike.')
                return None
            
            def produkt(vrstica, stolpec):
                produkt_ = 0
                for i in len(vrstica):
                    produkt_ += vrstica[i] * stolpec[i]
                return produkt_
            
            nova_matrika = []
            for vrstica in self.matrika:
                nova_vrstica = []
                for i in range(druga.n):
                    stolpec = []
                    for m in range(druga.m):
                        stolpec.append(
                                [vrstica[m] for vrstica in druga.matrika])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    