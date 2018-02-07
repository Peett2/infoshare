# nieskońcona pętla
# while True:
#     print('hello')

counter = 0
value = int(input('Podaj liczbę: \n'))

while counter < value:
    # within loop
    print('Hello',counter)
    counter += 1
# outside of loop
print('Bye')