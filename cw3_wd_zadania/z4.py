a=float(input('podaj a '))

def czy_ros(a):
    if a>0:
        print('funkcja rosnąca')
    if a<0:
        print('funkcja malejąca')
    if a==0:
        print('funkcja stała')

czy_ros(a)