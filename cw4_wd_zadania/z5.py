class C_Aryt:
    def __init__(self):
        self.a=1
        self.r=1
        self.n=1

    def wyświetl_dane(self):
        print("a=", +self.a, "r=", +self.r, "n=", +self.n)

    def pobierz_elementy(self, a1, a2, a3):
        if a3-a2!=a2-a1:
            return ("złe dane")
        self.r=a2-a1
        self.a=a1
        self.n=3

    def pobierz_parametry(self, a, r, n):
        self.a=a
        self.r=r
        self.n=n

    def policz_sume(self):
        print("suma to:", end=" ")
        return (((2*self.a)+((self.n-1)*self.r))*(self.n/2))

    def policz_elementy(self, ile):
        print("kolejne", +ile, "elementów to:", end=" ")
        for x in range (1,ile+1):
            print(self.a+(x-1)*self.r, end=" ")

ciag=C_Aryt()

ciag.wyświetl_dane()
print()

ciag.pobierz_elementy(2,4,6)
ciag.wyświetl_dane()
print(ciag.policz_sume())
print(ciag.policz_elementy(5))
print()

ciag.pobierz_parametry(2,1,7)
ciag.wyświetl_dane()
print(ciag.policz_sume())
print(ciag.policz_elementy(7))
