import math

a=float(input('długość pierwszej przyprostokątnej: '))
b=float(input('długość drugiej przyprostokątnej: '))

def pitagoras(a,b):
    return math.sqrt((a)**2+(b)**2)

print(pitagoras(a,b))
