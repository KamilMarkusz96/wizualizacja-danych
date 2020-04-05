przedmiotjednostka = {'dysk': 'szt','sok': 'l','papier': 'opakowanie',}
jednostkaprzedmiot = {value: key for key, value in przedmiotjednostka.items()}
print('Słownik:')
print(przedmiotjednostka)
print('Słownik po zamianie miejsc:')
print(jednostkaprzedmiot)