with open("zadanie_3.txt", "w") as plik:
    for x in range (0,10):
        l=x*x
        t=str(x)+"^2="+str(l)
        plik.writelines(str(t))
        plik.writelines("\n")

with open("zadanie_3.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")