class Ksztalty:

    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik

class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x = x
        self.y = x

    def __add__(self, other):
        return (self.x+other.x)

    def __ge__(self, other):
        if(self.x>=other.x):
            return (1)
        else:
            return (0)

    def __gt__(self, other):
        if(self.x>other.x):
            return (1)
        else:
            return (0)

    def __le__(self, other):
        if(self.x<=other.x):
            return (1)
        else:
            return (0)

    def __lt__(self, other):
        if(self.x<other.x):
            return 1
        else:
            return 0

    

kw0 = Kwadrat(5)
kw1 = Kwadrat(8)
kw01= Kwadrat(kw0+kw1)
print(kw0.x)
print(kw1.x)
print(kw01.x)