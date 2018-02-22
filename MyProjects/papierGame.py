from random import randint

lista = ['kamień', 'nożyce', 'papier']

user = input("Gramy w kamień-nożyce-papier. Wybierz jedno z poniższych:\n"
             "k - kamień, \n"
             "n - nożyce, \n"
             "p - papier:\n\n")

k = 'kamień'
n = 'nożyce'
p = 'papier'

import sys

if user == 'k':
    print('Twój wybór to \n', 'kamień', '\n komputer wybrał')
elif user == 'n':
    print('Twój wybór to \n', 'nożyce', '\n komputer wybrał')
elif user == 'p':
    print('Twój wybór to \n', 'papier', '\n komputer wybrał')
else:
    sys.exit('Niedozwolona wartość')

comp = randint(1, 3)
if comp == 1:
    comp = 'kamień'
elif comp == 2:
    comp = 'nożyce'
elif comp == 3:
    comp = 'papier'
# comp = 'k'
print(' ', comp)

if (user == 'kamień' and comp == 'nożyce') or (
        user == 'nożyce' and comp == 'papier') \
        or (user == 'papier' and comp == 'kamień'):
    print('Wygrywasz')
elif user == comp:
    print('Remis!')
else:
    print('Przegrywasz!!!')
