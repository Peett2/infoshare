text = 'Ala ma kota'
# for char in text:
#     print(char)

length = len(text)
# for idx in range(length):
#     print(text[idx])

some_range = range(length)
print(some_range)
is_loop_done  = False
for value in some_range:
    print(value)
    if value == length -1:
        is_loop_done = True
if is_loop_done:
    print('Hello')