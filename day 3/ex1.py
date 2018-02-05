# a=1
# b=2
# print(a+b)
# print(a-b)
# print(b**4)
# print(b^4)
#
# c=3
# print(c)
# c += 4  # c = c+4 compound operator - zmiana wartości zmiennej
# c -= 2
# c *= 2
# c /= 2
# print(c)
#
# print(c-1)
#
# c = c % 2
# print(c)

text='Ala ma kota'
text2='Tom\'s house' # escaping character
print(text2)

letter_a= text[0] # od początku index dodatni od 0
print('letter_a:',letter_a)
letter_t=text[-2] # od końca index negatywny bez zera
print('letter_t:',letter_t)

# length = len(text)
# print(length)
# last_char = text[length] # nie możliwe  bo ostatni znak to length -1
# print(last_char)

# slices

sth=text[3:8]
print('sth:',sth)

sth2=text[-4:-2]
print('sth2:',sth2)

steps=text[0:10:2]
print('steps:',steps)

print(text[0:15],'a')

text2=text[::-1]
print(text2)

print(text.upper())
print(text.lower())
