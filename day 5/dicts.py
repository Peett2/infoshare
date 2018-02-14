import copy

phonebook = {
    'Kowalski': 123,
    'Nowak': 456,
    'Iksinski': 789
}
# lastname = input('Podaj nazwisko:\n')
# pobieranie wartości z klucza kowalski:
# print (phonebook[lastname])

print(phonebook)

lastname = 'XYZ'
print(phonebook.get(lastname, 'Brak nazwiska w bazie'))

new_phonebook = phonebook.copy()
print(new_phonebook)
new_members = {'XYZ': 1, 'ABC': 2}
new_phonebook.update(new_members)
print(new_phonebook)

new_phonebook['XYZ'] = 0
print(new_phonebook)

new_phonebook.update({'XYZ': 5})
print(new_phonebook)

new_phonebook.update(Kowalski=898, Nowak=332)
print(new_phonebook)

del new_phonebook['XYZ']
print(new_phonebook)

for element in new_phonebook:
    print(element)

for key, value in new_phonebook.items():
    print(f'{key}->{value}')

only_keys = new_phonebook.keys()
print(only_keys)
values = new_phonebook.values()
print(values)
items = new_phonebook.items()
print(items)
