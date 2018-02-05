digit=int(input('podaj liczbe: \n'))

is_even = digit % 2

if not is_even:
        print('liczba jest parzysta')
else:
        print('liczba nie jest parzysta')