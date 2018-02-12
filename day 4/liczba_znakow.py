# program obliczajacy liczbe liter i cyfr w stringu

# ilosc_liter = str(len("Tomek36"))
# print(ilosc_liter)

string = input('Type in any string:\n')
digits = 0
letters = 0
others = 0

for char in string:
    if char.isdigit():
        digits+=1
    elif char.isalpha():
        letters +=1
    else:
        others +=1

print('Ciąg znaków posiada',digits,'cyfr,',letters,'liter oraz',others,'innych znaków')