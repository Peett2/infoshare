# wyświetl liczby parzyste od zera do zadanej liczby bez wykorzystania funkcji warunkowej

value = int(input('Podaj liczbę:\n'))

for digit in range(0,value,2):
    print(digit)