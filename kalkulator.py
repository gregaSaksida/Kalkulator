class Vektor:
    
    def __init__(self, vektor = [0, 0, 0]):
        self.vektor = vektor
    
    def __add__(self, drugi):
        if len(self.vektor) != len(drugi):
            return 'Vektorja nimata enakega števila komponent.'
        else:
            vsota = []
            for i, komponenta in enumerate(self.vektor):
                vsota.append(komponenta + drugi[i])
            return Vektor(vsota)
    
    def __mul__(self, drugi):
        skalar = True
        try:
            drugi + 0
        except:
            skalar = False
            
        if skalar:
            nov_vektor = []
            for i in range(len(self.vektor)):
                nov_vektor.append(drugi * self.vektor[i])
            return Vektor(nov_vektor)
        elif (not skalar) and len(self.vektor) == len(drugi):
            produkt = 0
            for i, komponenta in enumerate(self.vektor):
                produkt += komponenta * drugi[i]
            return produkt
        
        return 'Ali vektorja nimata enakega števila komponent ali eden od' + \
    ' njiju sploh ni vektor.'