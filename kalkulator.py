"""Ne pozabi:
    vektorski produkt
    determinante
    lastne vrednosti, vektorji
    potenciranje
	datoteke
	rang, inverzna
"""

"""Kalkulator računa z vektorji in matrikami."""

import math
import copy


class Vektor:
    
    """Ustvari razred vektorjev.
    Atributi:
        self.vektor,
        self.razseznost,
        self.je_vektor.
    Metode:
        __init__,
        __add__,
        __mul__,
        __sub__,
        desne verzije vseh naštetih računskih operacij,
        __repr__,
        __str__.
    Funkcije:
        dolzina,
        cos_kota,
        kot.
    """
    
    def __init__(self, vektor = [0, 0, 0]):
        
        self.vektor = list(vektor)
        self.razseznost = len(self.vektor)
        self.je_vektor = None
        """Obstoj atributa je_vektor služi kot edinstven pokazatelj,
        če je objekt res vektor. Vrednost atributa ni bistvena.
        """
    
    
    def __add__(self, drugi):
        
        try:
            drugi.je_vektor
            """Če objekt ni vektor, atribut je_vektor ne obstaja."""
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
            """Drugi operand je mogoče kakšen drug objekt, za katerega je
            množenje z vektorjem definirano (skalar).
            """     
        else:
            """Izvede se skalarno množenje."""
            if self.razseznost != drugi.razseznost:
                print('Množenja ni mogoče izvesti.'
                      ' Vektorja nista enako razsežna.')
                return None
            produkt = 0
            for i, komponenta in enumerate(self.vektor):
                produkt += komponenta * drugi.vektor[i]
            return produkt
        
        try:
            drugi.je_matrika
            """Razred matrik je definiran nižje v kodi. Ta del kode javi
            napako, če poskuša uporabnik levo množiti matriko z vektorjem
            (vektor * matrika).
            """
        except AttributeError:
            pass
        else:
            print('Vektorja ni mogoče množiti z matriko v tem vrstnem redu.')
            return None
        
        try:
            drugi + 0
        except TypeError or AttributeError:
            print('Množenja ni mogoče izvesti.'
                  ' Eden od operandov ni niti vektor niti skalar.')
            return None
        else:
            """Množenje vektorja s skalarjem."""
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
    """__radd__ in __rsub__ se aktivirata le, če levi operator ni vektor.
    Služita le nadzorovani sprožitvi napake.
    """
        
    
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
    return math.acos(cos_kota(vektor1, vektor2))
    
    
class Matrika:
    
    """Ustvari razred matrik.
    Atributi:
        self.matrika,
        self.m,
        self.n,
        self.je_matrika.
    Metode:
        __init__,
        __add__,
        __mul__,
        __sub__,
        desne verzije vseh naštetih računskih operacij,
        __repr__,
        __str__,
        transponirana.
    Funkcije:
        transponiranje.
    """
    
    def __init__(self, matrika = [[0, 0], [0, 0]]):
        self.matrika = list(matrika)
        self.m = len(self.matrika)    # Število vrstic matrike.
        for i in range(self.m):
            self.matrika[i] = list(self.matrika[i])
        self.n = len(self.matrika[0])    # Število stolpcev matrike.
        self.je_matrika = None
        """Obstoj atributa je_matrika služi kot edinstven pokazatelj,
        če je objekt res matrika. Vrednost atributa ni bistvena.
        """
    
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
        for j in range(self.n):
            stolpci.append([vrstica[j] for vrstica in self.matrika])
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
            """Seštevanje po vrsticah."""
            for i in range(self.m):
                vrstica = []
                for j in range(self.n):
                    vrstica.append(self.matrika[i][j] + druga.matrika[i][j])
                nova_matrika.append(vrstica)
            return Matrika(nova_matrika)
    
    
    def __mul__(self, druga):
        
        def produkt(vrstica, stolpec):
            produkt_ = 0
            for i in range(len(vrstica)):
                produkt_ += vrstica[i] * stolpec[i]
            return produkt_
        """Funkcija ustreza skalarnemu množenju dveh vektorjev."""
        
        def stolpec(matrika, i):
            stolpec_ = []
            for vrstica in matrika:
                stolpec_.append(vrstica[i])
            return stolpec_
        """Funkcija ustreza prepisu stolpca matrike v vrstico."""
        
        try:
            druga.je_matrika
        except AttributeError:
            pass
            """Drugi operand je mogoče kakšen drug objekt, za katerega je
            množenje z vektorjem definirano (skalar).
            """     
        else:
            if self.n != druga.m:
                print('Množenja ni mogoče izvesti. Število stolpcev prve'
                      ' matrike ni enako številu vrstic druge.')
                return None
            
            nova_matrika = []
            for vrstica in self.matrika:
                nova_vrstica = []
                for j in range(druga.n):
                    nova_vrstica.append(
                            produkt(vrstica, stolpec(druga.matrika, j)))
                nova_matrika.append(nova_vrstica)
            """Zavoljo večje enostavnosti kode se množenje posluži funkcij
            produkt in stolpec."""
            
            if len(nova_matrika) == 1 and len(nova_matrika[0]) == 1:
                return nova_matrika[0][0]
            elif len(nova_matrika) == 1:
                return Vektor(nova_matrika[0])
            elif len(nova_matrika[0]) == 1:
                return Vektor(stolpec(nova_matrika, 0))
            """Koda preveri, ali je produkt morda vektor ali pa skalar."""
            
            return Matrika(nova_matrika)
        
        try:
            druga.je_vektor
        except AttributeError:
            pass
        else:
            if self.n != druga.razseznost:
                print('Množenja ni mogoče izvesti. Razsežnost vektorja'
                      ' ne ustreza preslikavi.')
                return None
            nov_vektor = []
            for vrstica in self.matrika:
                nov_vektor.append(produkt(vrstica, druga.vektor))
            if len(nov_vektor) == 1:
                return nov_vektor[0]
            return Vektor(nov_vektor)
            """Koda preveri, ali je produkt morda skalar."""
        
        try:
            druga + 0
        except TypeError or AttributeError:
            print('Množenja ni mogoče izvesti. Eden od operandov ni niti'
                  ' matrika, niti vektor, niti skalar.')
            return None
        else:
            nova_matrika = copy.deepcopy(self.matrika)
            for i in range(self.m):
                for j in range(self.n):
                    nova_matrika[i][j] *= druga
            return Matrika(nova_matrika)
        """Če se velikost matrike ne spremeni, program ne preveri, ali je
        matrika morda vektor ali skalar. Zanaša se na predpostavko, da
        uporabnik ne bo nalašč ustvaril matrike, ki bi predstavljala zgolj
        vektor ali skalar. Tudi če bi, bi to gotovo naredil z določenim
        namenom."""
            
        
    def __sub__(self, druga):
        return self + (-1 * druga)
    
    def __radd__(self, napacen):
        return self + napacen

    def __rmul__(self, skalar):
        return self * skalar
    
    def __rsub__(self, napacen):
        return self - napacen
    """__radd__ in __rsub__ ponovno služita zgolj nadzorovanemu javljanju
    napak."""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    