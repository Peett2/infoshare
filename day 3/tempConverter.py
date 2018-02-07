# temerature converter C to F and F to C

temp = input('Podaj liczbę stopni w C lub F:\n').upper()

# check what type it is
#     C = (F - 32) * (5/9)
#     F = C * (9 / 5) + 32

value = int(temp[-10:-1])

if temp.endswith('C'):
    print('Podana temperatura w st. Cesjusza wynosi',
            value * (9/5)+32,'stopni Farenheita')
elif temp.endswith('F'):
    print('Podana temperatura w st. Farenheita wynosi',
         (value - 32) * (5/9), 'stopni Celsjusza')
else:
    print('Wpisz poprawną wartość temperatury.')