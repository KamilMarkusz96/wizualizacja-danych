import math

print('podaj współrzędne środka okręgu, oraz punktu który leży na okręgu')
a=float(input('środek wsp. x'))
b=float(input('środek wsp. y'))
x=float(input('pkt wsp. x'))
y=float(input('pkt wsp. y'))

def promień(a,b,x,y):
    return math.sqrt((a-x)**2+(b-y)**2)

print(promień(a,b,x,y))
