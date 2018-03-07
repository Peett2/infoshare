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

# my_list = list(range(1,11,2))
# print(my_list)
#
# text = 'Ala ma kota'
#
# txt_list = list(text)
# print(txt_list)
#
# # for txt_list in text:
# #     print(txt_list)
#
# for idx, element in enumerate(txt_list):
#     print(idx, element)
#
# for value in enumerate(txt_list):
#     print(value)
#
# my_list.append(13)
# print(my_list)
#
# my_list.reverse() # in place
# print(my_list)

my_list = list(range(10))
print(my_list)
print(hex(id(my_list)))

my_list2 = my_list.copy()
print(my_list2)
print(hex(id(my_list2)))

my_list3 = reversed(my_list2)
print(list(my_list3))
print(id(my_list3))
# print(type(my_list3))
# print(isinstance(my_list2, list))

# wyszukiwanie elementów
# print(my_list.index(None))

list_a = [1, 2, 3]
list_b = [4, 5, 6]
# list_a.append(list_b)
# print(list_a)
list_a.extend(list_b)
print(list_a)

list_c = [7, [8, 9]]
list_b.extend(list_c)
print(list_b)
