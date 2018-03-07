import os

FILENAME = 'dlugosc_pliku.txt'

print('plik do odczytu')
with open(FILENAME, 'r') as plik:
    coursor = plik.tell()
    print('przed oczytem')
    print(plik.read())
    print('po odczycie')
    coursor = plik.tell()
    print(coursor)
# print('plik do zapisu')
# with open(FILENAME, 'w') as plik:
#     print(plik.read())

print('tryb dopisywania')
with open(FILENAME, 'r+') as plik:
    coursor = plik.tell()
    print('pozycja kursora w trybie append', coursor)
    plik.seek(0)
    coursor = plik.tell()
    print('kursor przestawiony na pozycję: ', coursor)
    plik.write('ala ma kota, kot ma Ale\n')
