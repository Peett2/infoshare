value = input('Podaj dowolny ciąg znaków:\n')

while not value.isalpha() and not value.isdigit():
    print('Podałeś niepoprawne dane')
    value = input('Podaj dowolny ciąg znaków:\n')

if value.isdigit():
    print('Podałeś liczbę')
elif value.isalpha():
    print('Podałeś litery')

print('Bye')