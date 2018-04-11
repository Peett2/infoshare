# for n in range(2, 10):
#     print('n=', n)
#     for x in range(2, n):
#         print('x=', x)
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#          # loop fell through without finding a factor
#          print(n, 'is a prime number')

# zmienna na poziomie globalnym
imie = "jola"

def drukuj_imiona(imie_2):
    # uzywamy slowa global i nazwe zmiennej globalnej
    # jesli chcemy ja uzyc wewnatrz funkcji - niepolecane!
    global imie
    imie = "ania"

    imie = str(imie).capitalize()
    imie_2 = str(imie_2).capitalize()

    print(imie, imie_2)

# imiona takie same wypisano bo zmienna globalna
# zostala zmieniona wew. fukcji
drukuj_imiona("gosia")
print(imie)
