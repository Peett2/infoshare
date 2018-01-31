name = input('Wpisz swoje imie:\n')

# the bad way
print('Twoje imie to:',name)

# the good way
msg = 'Twoje imie to:\n'
print(msg, name)

# even better way
msg = f'Twoje imie to:\n{name}'
print(msg)