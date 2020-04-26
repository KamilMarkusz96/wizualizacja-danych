class Material:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.r=rodzaj
        self.dl=dlugosc
        self.szer=szerokosc

    def wyswietl_nazwe(self):
        return (self.r, self.dl, self.szer)

class Ubrania(Material):
    def __init__(self, rozmiar, kolor, dla_kogo):
        self.ro=rozmiar
        self.k=kolor
        self.dla=dla_kogo
    def wyswietl_dane(self):
        return (self.ro, self.k, self.dla)

class Sweter(Ubrania):
    def __init__(self,rodzaj_swetra):
        self.rodzaj=rodzaj_swetra

    def wyswietl_dane(self):
        return (self.rodzaj)

mat1=Material('bawelna', 40, 40)

print(mat1.wyswietl_nazwe())

ubr1=Ubrania('xxxl','czarny','meska')

print(ubr1.wyswietl_dane())

swe=Sweter('rozpinany')

print(swe.wyswietl_dane())
