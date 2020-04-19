import string

class Slowa:
    def __init__(self, wyraz1, wyraz2):
        self.w1 = wyraz1
        self.w2 = wyraz2
        self.dlw1 = len(wyraz1)
        self.dlw2 = len(wyraz2)

    def czy_palindrom(self):
        w1t = 1
        w2t = 1
        for x in range(0, self.dlw1):
            if self.w1[x] != self.w1[self.dlw1 -1 - x]:
                w1t = 0
        for x in range(0, self.dlw2):
            if self.w2[x] != self.w2[self.dlw2 -1 - x]:
                w2t = 0
        return ("Czy wyraz 1 to palidrom?",+w1t,"Czy wyraz 2 to palidrom?", w2t)

    def czy_metagram(self):
        t=1
        c1=0
        if self.dlw1 != self.dlw2:
            return ("wyrazy nie są metagramem")
        for x in range(0, self.dlw1-1):
            if self.w1[x]!=self.w2[x]:
                c1=1
            if (self.w1[x]!=self.w2[x] and c1==1):
                return ("wyrazy nie są metagramem")
        return ("wyrazy są metagramem")

    def czy_anagramy(self):

        if self.dlw1 != self.dlw2:
            return ("wyrazy nie są anagramem")
        for x in string.ascii_letters:
            if self.w1.count(x) != self.w2.count(x):
                return ("wyrazy nie są anagramami")
        return("wyrazy są anagramami")

    def wyswietl(self):
        print("wyraz 1 to: ", self.w1)
        print("wyraz 2 to: ", self.w2)


wyrazy = Slowa("kajak", "kamil")
wyrazy.wyswietl()
print(wyrazy.czy_palindrom())
print(wyrazy.czy_metagram())
print(wyrazy.czy_anagramy())

print()

wyrazy = Slowa("jaka", "kaja")
wyrazy.wyswietl()
print(wyrazy.czy_palindrom())
print(wyrazy.czy_metagram())
print(wyrazy.czy_anagramy())

print()

wyrazy = Slowa("kot", "kok")
wyrazy.wyswietl()
print(wyrazy.czy_palindrom())
print(wyrazy.czy_metagram())
print(wyrazy.czy_anagramy())
