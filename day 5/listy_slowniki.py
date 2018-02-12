# listy
# lista = [1,2,3,4,'dda']
#
# kopia_1 = lista.copy()
# kopia_2 = list(lista)
# kopia_3 = lista[:]

# print(lista[4]) # =dda

# # klucze
# slownik = {'ludzie': ['Ala', 'ola', 'pawel'], 'psy': ['szarik', 'reksio']}
#
# print(slownik.keys())
# print(slownik.values())

my_list = list(range(1,11,2))
print(my_list)

text = 'Ala ma kota'

txt_list = list(text)
print(txt_list)

# for txt_list in text:
#     print(txt_list)

for idx, element in enumerate(txt_list):
    print(idx, element)

for value in enumerate(txt_list):
    print(value)