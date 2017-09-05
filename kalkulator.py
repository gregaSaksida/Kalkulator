"""Kalkulator računa z vektorji in matrikami."""


""" PROGRAM """

import math
import copy

spominski_seznam = []
"""Seznam za beleženje zgodovine kalkulatorja."""

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
        __pow__,
        __eq__,
        __repr__,
        __str__.
    Funkcije:
        dolzina,
        cos_kota,
        kot,
        vektorski_produkt.
    """

    def __init__(self, vektor = [0, 0, 0]):
        
        self.vektor = list(vektor)
        self.razseznost = len(self.vektor)
        self.je_vektor = None
        """Obstoj atributa je_vektor služi kot edinstven pokazatelj,
        če je objekt res vektor. Vrednost atributa ni bistvena.
        """
        spominski_seznam.append(self)
    
    
    def __add__(self, drugi):
        
        try:
            drugi.je_vektor
            """Če objekt ni vektor, atribut je_vektor ne obstaja."""
        except AttributeError:
#            print('Seštevanja ni mogoče izvesti.'
#                  ' Eden od operandov ni vektor.')
            return('Seštevanja ni mogoče izvesti.'
                  ' Eden od operandov ni vektor.')
        
        else:
            if self.razseznost != drugi.razseznost:
#                print('Seštevanja ni mogoče izvesti.'
#                  ' Vektorja nista enako razsežna.')
                return('Seštevanja ni mogoče izvesti.'
                  ' Vektorja nista enako razsežna.')
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
#                print('Množenja ni mogoče izvesti.'
#                      ' Vektorja nista enako razsežna.')
                return('Množenja ni mogoče izvesti.'
                      ' Vektorja nista enako razsežna.')
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
#            print('Vektorja ni mogoče množiti z matriko v tem vrstnem redu.')
            return('Vektorja ni mogoče množiti z matriko v tem vrstnem redu.')
        
        try:
            drugi + 0
        except TypeError or AttributeError:
#            print('Množenja ni mogoče izvesti.'
#                  ' Eden od operandov ni niti vektor niti skalar.')
            return('Množenja ni mogoče izvesti.'
                  ' Eden od operandov ni niti vektor niti skalar.')
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
    
    def __pow__(self, eksponent):
        try:
            eksponent % 1
        except TypeError:
#            print('Potenciranja ni mogoče izvesti. Eksponent ni naravno'
#                  ' število.')
            return('Potenciranja ni mogoče izvesti. Eksponent ni naravno'
                  ' število.')
        else:
            if eksponent > 0 and eksponent % 1 == 0:
                nov_vektor = Vektor(copy.deepcopy(self.vektor))
                for i in range(eksponent - 1):
                    nov_vektor *= self
                return nov_vektor
            else:
#                print('Potenciranja ni mogoče izvesti. Eksponent ni naravno'
#                  ' število.')
                return('Potenciranja ni mogoče izvesti. Eksponent ni naravno'
                  ' število.')
    
    def __eq__(self, drugi):
        
        try:
            drugi.je_vektor
        except AttributeError:
            print('Elementa nista istega tipa (eden je vektor, drugi ne.')
            return False
        else:
            if self.razseznost != drugi.razseznost:
                return False
            for i in range(self.razseznost):
                if self.vektor[i] != drugi.vektor[i]:
                    return False
            return True
    
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

def vektorski_produkt(vektor1, vektor2):
    v1 = vektor1.vektor
    v2 = vektor2.vektor
    nov_vektor = [None, None, None]
    nov_vektor[0] = v1[1] * v2[2] - v2[1] * v1[2]
    nov_vektor[1] = - v1[0] * v2[2] + v2[0] * v1[2]
    nov_vektor[2] = v1[0] * v2[1] - v2[0] * v1[1]
    
    
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
        __pow__,
        __eq__,
        __repr__,
        __str__,
        transponirana.
    Funkcije:
        transponiranje,
		identicna,
        sled,
		permutacije,
		predznak_permutacije,
		determinanta.
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
        spominski_seznam.append(self)
    
    def __repr__(self):
        return 'Matrika({0})'.format(self.matrika)
    
    def __str__(self):
        if self.m < 20 and self.n < 20:
            for vrstica in self.matrika:
                print(vrstica)
        else:
            print(self.matrika)
        return '\n{0}x{1} matrika.'.format(self.m, self.n)

    
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

def identicna(n):
    identicna_matrika = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        identicna_matrika[i][i] = 1
    return Matrika(identicna_matrika)
    

class Matrika(Matrika):
    
    def __add__(self, druga):
        try:
            druga.je_matrika
        except AttributeError:
#            print('Seštevanja ni mogoče izvesti.'
#                  ' Eden od operandov ni matrika.')
            return('Seštevanja ni mogoče izvesti.'
                  ' Eden od operandov ni matrika.')
        
        else:
            if self.n != druga.n or self.m != druga.m:
#                print('Seštevanja ni mogoče izvesti.'
#                  ' Matriki nista enako veliki.')
                return('Seštevanja ni mogoče izvesti.'
                  ' Matriki nista enako veliki.')
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
#                print('Množenja ni mogoče izvesti. Število stolpcev prve'
#                      ' matrike ni enako številu vrstic druge.')
                return('Množenja ni mogoče izvesti. Število stolpcev prve'
                      ' matrike ni enako številu vrstic druge.')
            
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
#                print('Množenja ni mogoče izvesti. Razsežnost vektorja'
#                      ' ne ustreza preslikavi.')
                return('Množenja ni mogoče izvesti. Razsežnost vektorja'
                      ' ne ustreza preslikavi.')
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
#            print('Množenja ni mogoče izvesti. Eden od operandov ni niti'
#                  ' matrika, niti vektor, niti skalar.')
            return('Množenja ni mogoče izvesti. Eden od operandov ni niti'
                  ' matrika, niti vektor, niti skalar.')
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
    
    def __pow__(self, eksponent):
        try:
            eksponent % 1
        except TypeError:
#            print('Potenciranja ni mogoče izvesti. Eksponent ni nenegativno'
#                  ' celo število.')
            return('Potenciranja ni mogoče izvesti. Eksponent ni nenegativno'
                  ' celo število.')
        else:
            if eksponent > 0 and eksponent % 1 == 0:
                nova_matrika = Matrika(copy.deepcopy(self.matrika))
                for i in range(eksponent - 1):
                    nova_matrika *= self
                return nova_matrika
            elif eksponent == 0:
                return identicna(self.m)
            else:
#                print('Potenciranja ni mogoče izvesti. Eksponent ni nenegativno'
#                  ' celo število.')
                return('Potenciranja ni mogoče izvesti. Eksponent ni nenegativno'
                  ' celo število.')
    
    def __eq__(self, druga):
        
        try:
            druga.je_matrika
        except AttributeError:
            print('Elementa nista istega tipa (eden je matrika, drugi ne).')
            return False
        else:
            if self.m != druga.m or self.n != druga.n:
                return False
            for i in range(self.m):
                for j in range(self.n):
                    if self.matrika[i][j] != druga.matrika[i][j]:
                        return False
            return True
        
def sled(matrika):
    sled_ = 0
    for i in range(matrika.m):
        sled_ += matrika.matrika[i][i]
    return sled_


def permutacije(n):
    """Pomožna funkcija za funkcijo "determinanta".
    Vrne vse permutacije števil od 0 do n-1.
    """
    if n == 0:
        return {()}
    else:
        trenutne_permutacije = permutacije(n - 1)
        """Rekurzija."""
        nove_permutacije = set()
        
        for permutacija in trenutne_permutacije:
            for i in range(len(permutacija) + 1):
                nove_permutacije.add(
                        permutacija[:i] + (n - 1, ) + permutacija[i:])
                """Obstoječim permutacijam vrine število."""
        return nove_permutacije

def predznak_permutacije(perm):
    """Pomožna funkcija za funkcijo "determinanta".
    Vrne predznak permutacije.
    """
    inverzije = 0
    for pozicija, stevilo in enumerate(perm):
        for _ in perm[(pozicija + 1):]:
            if _ < stevilo:
                inverzije += 1
    if inverzije % 2 == 0:
        return 1
    else:
        return - 1

def determinanta(matrika):
    determinanta = 0
    permutacije_ = permutacije(matrika.m)
    for permutacija in permutacije_:
        delna_det = 1
        for i in range(matrika.m):
            delna_det *= matrika.matrika[i][permutacija[i]]
            """Na vsakem koraku notranje "for" zanke iz permutacije
            izbere naslednji indeks."""
        determinanta += predznak_permutacije(permutacija) * delna_det
    return determinanta


###############################################################
###############################################################


""" GRAFIČNI VMESNIK """
        
import tkinter as tk


""" Skalarni kalkulator """

simbol = None
operand = None

trenutno_stevilo = 0

okno = tk.Tk()
skalarni_kalkulator = tk.Frame(okno)
skalarni_kalkulator.grid(row=1, column=0)
tk.Label(okno, text='Skalarni kalkulator').grid(row=0, column=0)

vhod = tk.Entry(skalarni_kalkulator)
vhod.pack()

ukazi_zgornji = tk.Frame(skalarni_kalkulator)
ukazi_zgornji.pack()

ukazi = tk.Frame(skalarni_kalkulator)
ukazi.pack()


def izpis(vrednost):
    if vrednost != ',' or ',' not in vhod.get():
        vhod.insert(len(vhod.get()), vrednost)

def operacija(simbol_):
    global simbol
    global operand
    simbol = simbol_
    operand = float(vhod.get().replace(',', '.'))
    vhod.delete(0, 'end')

def izracun():
    global simbol
    global operand
    
    if vhod.get() == None or vhod.get() == '':
        drugi_operand = 0
    else:
        drugi_operand = float(vhod.get().replace(',', '.'))
    
    if operand == None or simbol == None:
        rezultat = drugi_operand
    elif simbol == '+':
        rezultat = operand + drugi_operand
    elif simbol == '-':
        rezultat = operand - drugi_operand
    elif simbol == '*':
        rezultat = operand * drugi_operand
    elif simbol == '/':
        rezultat = operand / drugi_operand
    elif simbol == '**':
        rezultat = operand ** drugi_operand
    elif simbol == '==':
        if operand == drugi_operand:
            rezultat = 'Drži.'
        else:
            rezultat = 'Ne drži.'
        
    vhod.delete(0, 'end')
    vhod.insert(0, rezultat)
    simbol = None
    operand = None

def nasprotje():
    if vhod.get() == None or vhod.get() == '':
        nasprotna_vrednost = 0
    else:
        nasprotna_vrednost = (-1) *  float(vhod.get().replace(',', '.'))
    vhod.delete(0, 'end')
    vhod.insert(0, nasprotna_vrednost)

def pi():
    vhod.insert('end', math.pi)

def e():
    vhod.insert('end', math.e)
    

def izbrisi_eno():
    vhod.delete(len(vhod.get()) - 1, 'end')

def izbrisi_vhod():
    vhod.delete(0, 'end')

def izbrisi_proces():
    vhod.delete(0, 'end')
    global simbol
    global operand
    simbol = None
    operand = None

def vstavi():
    vhod2.insert('end', vhod.get())

tk.Button(ukazi, text = '1', command=lambda: izpis(1)).grid(row=2, column=0)
tk.Button(ukazi, text = '2', command=lambda: izpis(2)).grid(row=2, column=1)
tk.Button(ukazi, text = '3', command=lambda: izpis(3)).grid(row=2, column=2)
tk.Button(ukazi, text = '4', command=lambda: izpis(4)).grid(row=1, column=0)
tk.Button(ukazi, text = '5', command=lambda: izpis(5)).grid(row=1, column=1)
tk.Button(ukazi, text = '6', command=lambda: izpis(6)).grid(row=1, column=2)
tk.Button(ukazi, text = '7', command=lambda: izpis(7)).grid(row=0, column=0)
tk.Button(ukazi, text = '8', command=lambda: izpis(8)).grid(row=0, column=1)
tk.Button(ukazi, text = '9', command=lambda: izpis(9)).grid(row=0, column=2)
tk.Button(ukazi, text = '0', command=lambda: izpis(0)).grid(row=3, column=0)

tk.Button(ukazi, text = ',', command=lambda: izpis(',')).grid(row=3, column=1)
tk.Button(ukazi, text = 'π', command=pi).grid(row=2, column=3)
tk.Button(ukazi, text = 'e', command=e).grid(row=3, column=3)
tk.Button(ukazi, text = 'CE', command=izbrisi_vhod).grid(row=0, column=4)
tk.Button(ukazi, text = 'AC', command=izbrisi_proces).grid(row=0, column=5)


for i in range(2):
    tk.Button(ukazi, text = '').grid(row=i, column=3)
tk.Button(ukazi, text = '').grid(row=3, column=2)
    
tk.Button(ukazi, text = '=', command=izracun).grid(row=3, column=4)
tk.Button(ukazi, text = '==', command=lambda: operacija('==')).grid(
        row=3, column=5)
tk.Button(ukazi, text = '+', command=lambda: operacija('+')).grid(
        row=2, column=4)
tk.Button(ukazi, text = '-', command=lambda: operacija('-')).grid(
        row=2, column=5)
tk.Button(ukazi, text = 'x', command=lambda: operacija('*')).grid(
        row=1, column=4)
tk.Button(ukazi, text = '/', command=lambda: operacija('/')).grid(
        row=1, column=5)

tk.Button(ukazi_zgornji, text = 'a^b', command=lambda: operacija('**')).grid(
        row=0, column=0)
tk.Button(ukazi_zgornji, text = 'del', command=izbrisi_eno).grid(
        row=0, column=1)
tk.Button(ukazi_zgornji, text = '+-', command=nasprotje).grid(row=0, column=2)
tk.Button(ukazi_zgornji, text = 'vstavi', command=vstavi).grid(row=0, column=3)


tk.Label(okno, text='|').grid(row=0, column=1)
vmesni_prostor=tk.Frame(okno)
vmesni_prostor.grid(row=1, column=1)
for i in range(6):
    tk.Label(vmesni_prostor, text='|').grid(row=i, column=1)


###############################################################
###############################################################


""" Matrični kalkulator """

matricni_kalkulator = tk.Frame(okno)
matricni_kalkulator.grid(row=1, column=2)
tk.Label(okno, text='Matrični kalkulator').grid(row=0, column=2)

vhod2 = tk.Entry(matricni_kalkulator, width=70)
vhod2.pack()

ukazi_zgornji2 = tk.Frame(matricni_kalkulator)
ukazi_zgornji2.pack()

ukazi2 = tk.Frame(matricni_kalkulator)
ukazi2.pack()
izhod_ = tk.Frame(okno)
izhod_.grid(row=1, column=3)
izhod = tk.Text(izhod_, height = 30)
izhod.pack()


class Matrika(Matrika):
    def izpisi_se(self):
        for vrstica in self.matrika:
            izhod.insert('insert', vrstica)
            izhod.insert('insert', '\n')
        izhod.insert('insert', '{0}x{1} matrika.'.format(self.m, self.n))


simbol2 = None
operand2 = None
matrika = False
vektor = False
matrika_prava = None
vektor_pravi = None


def izpis2(vrednost):
    if vrednost != ',' or ',' not in vhod2.get():
        vhod2.insert(len(vhod2.get()), vrednost)

def operacija2(simbol_):
    global simbol2
    global operand2
    global matrika_prava
    global vektor_pravi
    simbol2 = simbol_
    if matrika_prava:
        operand2 = matrika_prava
    elif vektor_pravi:
        operand2 = vektor_pravi
    elif vhod2.get() != '':
        operand2 = float(vhod2.get().replace(',', '.'))
    else:
        simbol2 = None
    vhod2.delete(0, 'end')
    matrika_prava = None
    vektor_pravi = None

def izracun2():
    global simbol2
    global operand2
    global matrika_prava
    global vektor_pravi
    
    if matrika_prava:
        drugi_operand = matrika_prava
    elif vektor_pravi:
        drugi_operand = vektor_pravi
    elif vhod2.get() != '':
        drugi_operand = float(vhod2.get().replace(',', '.'))
    else:
        vhod2.delete(0, 'end')
        vhod2.insert(0, 0)
        simbol2 = None
        operand2 = None
        return None
    
    if operand2 == None or simbol2 == None:
        rezultat = drugi_operand
    elif simbol2 == '+':
        rezultat = operand2 + drugi_operand
    elif simbol2 == '-':
        rezultat = operand2 - drugi_operand
    elif simbol2 == '*':
        rezultat = operand2 * drugi_operand
    elif simbol2 == '/':
        rezultat = operand2 / drugi_operand
    elif simbol2 == '**':
        rezultat = operand2 ** drugi_operand
    elif simbol2 == 'cos':
        rezultat = cos_kota(operand2, drugi_operand)
    elif simbol2 == 'kot':
        rezultat = kot(operand2, drugi_operand)
    elif simbol2 == 'vektorski':
        rezultat = vektorski_produkt(operand2, drugi_operand)
    elif simbol2 == '==':
        if operand2 == drugi_operand:
            rezultat = 'Drži.'
        else:
            rezultat = 'Ne drži.'
        
    vhod2.delete(0, 'end')
    try:
        rezultat.je_matrika
    except AttributeError:
        vhod2.insert(0, rezultat)
    else:
        izhod.delete('0.0', 'end')
        rezultat.izpisi_se()
    simbol2 = None
    operand2 = None
    matrika_prava = None
    vektor_pravi = None

def nasprotje2():
    if vhod2.get() == None or vhod2.get() == '':
        nasprotna_vrednost = 0
    else:
        nasprotna_vrednost = (-1) *  float(vhod2.get().replace(',', '.'))
    vhod2.delete(0, 'end')
    vhod2.insert(0, nasprotna_vrednost)

def pi2():
    vhod2.insert('end', math.pi)

def e2():
    vhod2.insert('end', math.e)
    

def izbrisi_eno2():
    vhod2.delete(len(vhod2.get()) - 1, 'end')

def izbrisi_vhod2():
    vhod2.delete(0, 'end')

def izbrisi_proces2():
    vhod2.delete(0, 'end')
    izhod.delete('0.0', 'end')
    global simbol2
    global operand2
    global matrika
    global vektor
    global matrika_prava
    global vektor_pravi
    simbol2 = None
    operand2 = None
    matrika = None
    vektor = None
    matrika_prava = None
    vektor_pravi = None

tk.Button(ukazi2, text = '1', command=lambda: izpis2(1)).grid(row=2, column=0)
tk.Button(ukazi2, text = '2', command=lambda: izpis2(2)).grid(row=2, column=1)
tk.Button(ukazi2, text = '3', command=lambda: izpis2(3)).grid(row=2, column=2)
tk.Button(ukazi2, text = '4', command=lambda: izpis2(4)).grid(row=1, column=0)
tk.Button(ukazi2, text = '5', command=lambda: izpis2(5)).grid(row=1, column=1)
tk.Button(ukazi2, text = '6', command=lambda: izpis2(6)).grid(row=1, column=2)
tk.Button(ukazi2, text = '7', command=lambda: izpis2(7)).grid(row=0, column=0)
tk.Button(ukazi2, text = '8', command=lambda: izpis2(8)).grid(row=0, column=1)
tk.Button(ukazi2, text = '9', command=lambda: izpis2(9)).grid(row=0, column=2)
tk.Button(ukazi2, text = '0', command=lambda: izpis2(0)).grid(row=3, column=0)

tk.Button(ukazi2, text = ',', command=lambda: izpis2(',')).grid(row=3, column=1)
tk.Button(ukazi2, text = 'π', command=pi2).grid(row=2, column=3)
tk.Button(ukazi2, text = 'e', command=e2).grid(row=3, column=3)
tk.Button(ukazi2, text = 'CE', command=izbrisi_vhod2).grid(row=0, column=4)
tk.Button(ukazi2, text = 'AC', command=izbrisi_proces2).grid(row=0, column=5)


for i in range(2):
    tk.Button(ukazi2, text = '').grid(row=i, column=3)
    
tk.Button(ukazi2, text = '=', command=izracun2).grid(row=3, column=4)
tk.Button(ukazi2, text = '==', command=lambda: operacija2('==')).grid(
        row=3, column=5)
tk.Button(ukazi2, text = '+', command=lambda: operacija2('+')).grid(
        row=2, column=4)
tk.Button(ukazi2, text = '-', command=lambda: operacija2('-')).grid(
        row=2, column=5)
tk.Button(ukazi2, text = 'x', command=lambda: operacija2('*')).grid(
        row=1, column=4)
tk.Button(ukazi2, text = '/', command=lambda: operacija2('/')).grid(
        row=1, column=5)

tk.Button(ukazi_zgornji2, text = 'a^b', command=lambda: operacija2('**')).grid(
        row=0, column=0)
tk.Button(ukazi_zgornji2, text = 'del', command=izbrisi_eno2).grid(
        row=0, column=1)
tk.Button(ukazi_zgornji2, text = '+-', command=nasprotje2).grid(row=0, column=2)


""" Dodatne funckije matričnega kalkulatorja """

def M():
    global matrika
    global vrstice
    global matrika_prava
    
    if matrika:
        if vrstice:
            matrika_prava = Matrika(vrstice)
    else:
        vrstice = []
    
    matrika = not matrika


def V():
    global vektor
    vektor = not vektor

def potrdi():
    global matrika
    global vektor
    global vektor_pravi
    if matrika:
        global vrstice
        seznam = vhod2.get().split(';')
        for i in range(len(seznam)):
            seznam[i] = float(seznam[i].replace(',', '.'))
        vrstice.append(seznam)
        vhod2.delete(0, 'end')
    
    elif vektor:
        seznam = vhod2.get().split(';')
        for i in range(len(seznam)):
            seznam[i] = float(seznam[i].replace(',', '.'))
        vektor_pravi = Vektor(seznam)
    
    vhod2.delete(0, 'end')


def dolzina_():
    global vektor_pravi
    rezultat = dolzina(vektor_pravi)
    vektor_pravi = None
    vhod2.delete(0, 'end')
    vhod2.insert(0, rezultat)


def trans():
    global matrika_prava
    matrika_prava.transponirana()
    vhod2.delete(0, 'end')
    izhod.delete('0.0', 'end')
    matrika_prava.izpisi_se()

def identicna_():
    global matrika_prava
    n = int(vhod2.get())
    matrika_prava = identicna(n)
    vhod2.delete(0, 'end')
    izhod.delete('0.0', 'end')
    matrika_prava.izpisi_se()

def sled_():
    global matrika_prava
    vhod2.delete(0, 'end')
    vhod2.insert(0, sled(matrika_prava))
    matrika_prava = None

def det():
    global matrika_prava
    vhod2.delete(0, 'end')
    vhod2.insert(0, determinanta(matrika_prava))
    matrika_prava = None


tk.Button(ukazi2, text = ';', command=lambda: izpis2(';')).grid(row=3, column=2)
tk.Button(ukazi2, text = 'V', command=V).grid(
        row=0, column=6)
tk.Button(ukazi2, text = 'M', command=M).grid(row=1, column=6)
tk.Button(ukazi2, text = '⏎', command=potrdi).grid(row=2, column=6)

tk.Button(ukazi2, text = 'dolžina', command=dolzina_).grid(row=0, column=7)
tk.Button(ukazi2, text = 'cos kota', command=lambda: operacija2('cos')).grid(
        row=1, column=7)
tk.Button(ukazi2, text = 'kot', command=lambda: operacija2('kot')).grid(
        row=2, column=7)
tk.Button(ukazi2, text = 'vekt. pr.', command=lambda: operacija2(
        'vektorski')).grid(row=3, column=7)

tk.Button(ukazi2, text = 'trans.', command=trans).grid(row=0, column=8)
tk.Button(ukazi2, text = 'ɪ', command=identicna_).grid(row=1, column=8)
tk.Button(ukazi2, text = 'sled', command=sled_).grid(row=2, column=8)
tk.Button(ukazi2, text = 'det', command=det).grid(row=3, column=8)


tk.Label(okno, text='Navodila:').grid(row=0, column=4)
tk.Label(okno, text=(
        'Levi kalkulator je namenjen računanju\n'
        ' s števili med vpisovanjem matrik ali \n'
        'vektorjev v desnem kalkulatorju.\n'
        '\n'
        'Kalkulator lahko hkrati izvede le eno\n'
        'računsko operacijo. Za vsako izbrano\n'
        'operacijo morate klikniti tipko "="\n'
        'natanko enkrat. Primer: proces\n'
        '3+4+5 ni dovoljen.\n'
        'Proces 3+4=; +5= je.\n'
        '\n'
         'Tipke: del: izbriše zadnji vpisani znak, \n'
         'vstavi: število iz skalarnega kalkulatorja \n'
         'vstavi v matričnega, \n'
         'CE: počisti vpisno polje, \n'
         'AC: ponastavi kalkulator. \n'
         'ɪ: vrne identično matriko želene\n'
         'dimenzije.\n'
         '\n'
         'Elemente in operacije vpisujte v takem \n'
         'vrstnem redu, kot bi jih, če bi jih \n'
         'pisali na roko. Tipka = izvede \n'
         'operacijo in ponastavi kalkulator. \n'
         'Operacija == preverja enakost elementov,\n'
         'uporabljajte jo, kot vse ostale operacije.\n'
         '\n'
         'Matrični kalkulator:\n'
         'za vpis vektorja kliknite tipko "V",\n'
         ' komponente vektorja ločite s podpičjem\n'
         ' (desno od decimalne vejice). Ko \n'
         'končate, pritisnite tipko ⏎.\n'
         '\n'
         'Za vpis matrike kliknite tipko "M".\n'
         'Vnesite prvo vrstico matrike, njene\n'
         'komponente ločite s podpičjem. Ko\n'
         'vnesete celotno vrstico, kliknite\n'
         'tipko ⏎ ter vnesite drugo vrstico.\n'
         '⏎ kliknite tudi po vnostu zadnje\n'
         'vrstice, nakar ponovno kliknite\n'
         'tipko "M".'
         '\n')).grid(row=1, column=4)



okno.mainloop()
    
    
    
    
    
    
    
    
    
    
    