import os

# constant value
FILENAME = 'dlugosc_pliku.txt'

file_size = os.path.getsize(FILENAME)
print(f'Rozmiar pliku: {file_size}')

with open(FILENAME) as plik:
    total_chars = 0
    for line in plik:
        # linia pliku
        # print(char)
        total_chars += len(line)
    print(total_chars)

with open(FILENAME) as plik:
    print(plik.readlines())
