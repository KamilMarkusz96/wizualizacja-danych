import random

macierz = [[random.randint(0, 9) for i in range (0, 4, 1)] for j in range (0, 4, 1)]
przekatna = [macierz[i][j] for j in range (0, 4, 1) for i in range (0, 4, 1) if i == j]
print(macierz)
print('Przekątna: ',przekatna)