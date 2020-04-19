class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa=nazwa_produktu
        self.ilosc=ilosc
        self.jednostka_miary=jednostka_miary
        self.cena_jed=cena_jed

    def wyswietl_produkt(self):
        return (self.nazwa, self.ilosc, self.jednostka_miary, self.cena_jed)

    def ile_produktu(self):
        return(self.ilosc, self.jednostka_miary)

    def ile_kosztuje(self):
        return(self.ilosc * self.cena_jed)

ziemniak=NaZakupy('ziemniaki',3,'kg',3)

print(ziemniak.wyswietl_produkt())
print(ziemniak.ile_produktu())
print(ziemniak.ile_kosztuje())