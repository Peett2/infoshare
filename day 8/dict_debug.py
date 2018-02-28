people = {
    'kowalski': 'jan',
    'nowak': 'jacek'
}

lastname = input('podaj nazwisko:\n')

# bad
if lastname in people:
    print(people[lastname])

# better
# message = 'nie ma nazwiska w bazie'
# print(people.get(lastname,message))

# the best
try:
    print(people[lastname])
except KeyError as keyerr:
    print(f'Nie ma takiego nazwiska jak: {keyerr}')

filename = input('podaj nazwe pliku:\n')

try:
    plik = open(filename)
    print(plik.read())
except FileNotFoundError as error:
    print(f'Pliku nie znaleziono: {error.filename}')
finally:
    print('goodbye')