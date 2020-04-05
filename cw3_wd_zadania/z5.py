a_1=float(input('podaj a_1 '))
a_2=float(input('podaj a_2 '))

def położenie(a_1,a_2):
    if a_1==a_2:
        print('funkcje równoległe')
    elif a_1*a_2==-1:
        print('funkcje prostopadłe')
    else :
        print('funkcje nie są ani równloległe ani prostopadłe')

położenie(a_1,a_2)