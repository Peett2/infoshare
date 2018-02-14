from random import randint

k = 'kamień'
n = 'nożyce'
p = 'papier'

user = input("Gramy w kamień-nożyce-papier. Wybierz jedno z poniższych:\n"
             "k - kamień, \n"
             "n - nożyce, \n"
             "p - papier:\n\n")

import sys

if user == 'k':
    print('Twój wybór to \n', k, '\n komputer wybrał')
elif user == 'n':
    print('Twój wybór to \n', n, '\n komputer wybrał')
elif user == 'p':
    print('Twój wybór to \n', p, '\n komputer wybrał')
else:
    sys.exit('Niedozwolona wartość')

# comp = randint(1,3)
# if comp == 1:
#     comp = k
# elif comp == 2:
#     comp = n
# elif comp == 3:
#     comp = p
comp = 'k'
print(' ', comp)

if (user == k and comp == n) or (user == n and comp == p) \
        or (user == p and comp == k):
    print('Wygrywasz')
elif user == comp:
    print('Remis!')
else:
    print('Przegrywasz!!!')
