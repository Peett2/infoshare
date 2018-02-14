from random import randint

number = int(input("Podaj dowolną liczbę od 0 do 99:\n"))

random_number = randint(0, 99)

if len(str(number)) > 2:
    print('Za duża liczba - oszukujesz')
elif number < random_number:
    print('Moja liczba to', random_number,
          '\nTwoja liczba jest mniejsza - PRZEGRYWASZ')
elif number > random_number:
    print('Moja liczba to', random_number,
          '\nTwoja liczba jest większa - WYGRYWASZ')
else:
    print('Mamy remis :)')
