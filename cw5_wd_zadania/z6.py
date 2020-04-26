class Wspak:
    def __init__(self, dane):
        self.dane=dane
        self.ind=len(dane)

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind == 0:
            raise StopIteration
        self.ind = self.ind - 1
        return self.dane[self.ind]

tablica = Wspak([1, 2, 3])
print('tablica [1, 2, 3]', end=' ')
print('[', end='')
print(next(tablica), end=', ')
print(next(tablica), end=', ')
print(next(tablica), end=']')
print()

imie = Wspak('Kamil')
print('Kamil :', end=' ')
print(next(imie), end='')
print(next(imie), end='')
print(next(imie), end='')
print(next(imie), end='')
print(next(imie))