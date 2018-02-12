from collections import defaultdict, Counter
#
# my_dict = defaultdict(int)
# print(my_dict['non_existing'])

#  @todo zliczyć ile razy występuje każdy znak w stringu - wykorzystać słownik

text = 'ala ma kota, kot ma ale'
my_dict = dict()

# the bad way

for char in text:
    if char in my_dict:
        my_dict[char] += 1
    else:
        my_dict[char] = 1
print(my_dict)

# better way

my_dict2 = defaultdict(int)
for char in text:
    my_dict2[char] += 1
print(my_dict2)

print(my_dict2 == my_dict)
# best way
print(Counter(text))

