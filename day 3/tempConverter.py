# temerature converter C to F and F to C

temp = input('Podaj liczbę stopni w C lub F:\n').upper()

# check what type it is
#     C = (F - 32) * (5/9)
#     F = C * (9 / 5) + 32

value = int(temp[-10:-1])

if temp.endswith('C'):
    print('Podana temperatura w Farenheitach wynosi',
            value * 9/5+32,'stopni Celsjusza')
elif temp.endswith('F'):
    print('Podana temperatura w Celsjuszach wynosi',
         (value - 32) * (5/9), 'stopni Farenheita')
else:
    print('Wpisz poprawną wartość temperatury.')