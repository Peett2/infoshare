# with open('osoby') as plik:
#     header = plik.readline()
#     header = header.strip()
#     name, lastname, age = header.split(',')
#     print(f'{name} | {lastname} | {age}')
#     print('________________')
#     for line in plik:
#         print(line.strip())
#
# FORMAT = '{name},{lastname},{age}\n'
# name = input('Podaj imię:\n')
# lastname = input('Podaj nazwisko:\n')
# age = input('Podaj wiek:\n')
#
# with open('osoby', 'a') as plik:
#     plik.write(FORMAT.format(name=name, lastname=lastname, age=age))

import csv

with open('osoby') as plik:
    reader = csv.reader(plik)
    for line in reader:
        print(line)

data = ['Jan', 'Kowalski', 45]

with open('osoby', 'a') as plik:
    writer = csv.writer(plik)
    writer.writerow(data)