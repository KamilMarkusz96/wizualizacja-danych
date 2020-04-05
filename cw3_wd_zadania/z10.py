def ilosc(**lista):
    suma = 0.0
    for i in lista:
        suma = suma + float(lista[i])
    return suma

print('ilość rzeczy do kupienia: ', ilosc(chleb=2, ołówek=1, sok=1, ser=2, pomidor=2))