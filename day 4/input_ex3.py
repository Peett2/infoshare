value = input('Podaj liczbę:\n')

while not value.isdigit() or int(value) == 0:
    print('Podałeś niepoprawne dane')
    value = input('Podaj liczbę różną od zera:\n')

print('Bye')