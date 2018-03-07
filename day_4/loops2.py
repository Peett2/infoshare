counter = 0
value = int(input('Podaj liczbę: \n'))

while counter < value:
    # within loop
    if counter % 2:
        print(counter)
        counter += 1
    elif value > 1000:
        break
    else:
        counter += 1
        continue
# outside of loop
print('Bye')
