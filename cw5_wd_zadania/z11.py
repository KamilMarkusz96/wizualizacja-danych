def ciag_fibo():
    a=0
    b=1
    while a>-1:
        b=a+b
        a=b-a
        yield b-a

fibo=ciag_fibo()
print('kolejne 10 wyrazow ciagu fibonacciego to',end=': ')
for i in range(0, 10):
    print(next(fibo), end=' ')