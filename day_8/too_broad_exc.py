digits= {
    'cztery': '4',
    'dwa': '2'
}

digit = input('Podaj liczbe:\n')


try:
    result = digits[digit] - digits['dwa']
    print(plik.read())
except KeyError as keyError:
    print(f'Nie ma takiego klucza jak: {keyError}')
except TypeError as typeerr:
    print(f'typerrror: {typeerr}')
finally:
    print('Goodbye')