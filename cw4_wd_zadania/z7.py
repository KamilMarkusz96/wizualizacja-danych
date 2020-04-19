class Robaczek:
    def __init__(self, x, y, krok):
        self.x=x
        self.y=y
        self.krok=krok

    def zmien_robaczka(self, x1, y1, krok1):
        self.x=x1
        self.y=y1
        self.krok=krok1

    def gora(self, ile):
        self.y += ile*self.krok

    def dol(self, ile):
        self.y -= ile * self.krok

    def prawo(self, ile):
        self.x += ile * self.krok

    def lewo(self, ile):
        self.x -= ile * self.krok

    def gdzie_jestes(self):
        return(self.x, self.y)

print("podstawowy robaczek Rob o wsp: x=0, y=0 i kroku=1")
Rob=Robaczek(0, 0, 1)
print("Rob.gora(2)")
Rob.gora(2)
print(Rob.gdzie_jestes())
print("Rob.prawo(3)")
Rob.prawo(3)
print(Rob.gdzie_jestes())
print("Rob.dol(3)")
Rob.dol(3)
print(Rob.gdzie_jestes())
print("Rob.lewo(1)")
Rob.lewo(1)
print(Rob.gdzie_jestes())
print()
print("zmiana ustawień robaczka Roba na x=2, y=3 i krok=2")
Rob.zmien_robaczka(2,3,2)
print("Rob.gora(2)")
Rob.gora(2)
print(Rob.gdzie_jestes())
print("Rob.prawo(3)")
Rob.prawo(3)
print(Rob.gdzie_jestes())
print("Rob.dol(3)")
Rob.dol(3)
print(Rob.gdzie_jestes())
print("Rob.lewo(1)")
Rob.lewo(1)
print(Rob.gdzie_jestes())