# pobierz od użytkownika dowolny znak
# sprawdź czy wprowadzona dana to liczba czy litera
# wyświetl stosowny komunikat 'wprowdziłeś dane typu: <type>

value = input('Podaj dowolny ciąg znaków:\n')

if value.isdigit():
    print('Podałeś liczbę')
    print('Bye')
elif value.isalpha():
    print('Podałeś litery')
    print('Bye')
else:
    print('HELP')
