number = input('Podaj dowolną liczbę:\n')

if number.isdigit() and int(number)!=0:
    number = int(number)
    if not number % 3:
        print('Liczba jest podzielna przez 3 a wynik to: ',int(number / 3))
    else:
        print('Liczba nie jest podzielna przez 3.')

    if not number % 5:
        print('Liczba jest podzielna przez 5 a wynik to: ', int(number / 5))
    else:
        print('Liczba nie jest podzielna przez 5.')

    if not number % 7:
        print('Liczba jest podzielna przez 7 a wynik to: ', int(number / 7))
    else:
        print('Liczba nie jest podzielna przez 7.')
else:
    print('Mogę sprawdzać tylko liczby całkowite!')