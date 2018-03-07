# program obliczajacy liczbe liter i cyfr w stringu

# ilosc_liter = str(len("Tomek36"))
# print(ilosc_liter)

string = input('Wpisz dowolny ciąg znaków:\n')

while len(string) < 1:
    string = input('Musi być co najmniej jeden znak. '
                   'Wpisz dowolny ciąg jeszcze raz:\n')

digits = 0
letters = 0
others = 0

for char in string:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1
    else:
        others += 1

print('\nCiąg znaków posiada:\n', digits, 'cyfr,\n', letters,
      'liter oraz\n', others, 'innych znaków')