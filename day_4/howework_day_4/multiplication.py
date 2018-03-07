# program wypisujący tabliczkę mnozenia (1 do 10) dla podanej przez użytkownika liczby
# np: 3 x 1 = 3
#     3 x 2 = 6
#     3 x 3 = 9 itp

number = int(input('Podaj liczbę:\n'))

multiplier = 1

while multiplier <= 10:
    print(number, '*', multiplier, '=',
          number * multiplier)
    multiplier += 1