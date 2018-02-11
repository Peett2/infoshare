# wypisac liczby od 1 do 100, ktore naleza do ciagu fibonacciego
#
# 0, 1, 1, 2, 3, 5, 8, 13
#
#  [x - 2] + [x -1] = [x]

# y = x - 2

# x = x -1

x = 0
y = 1

print(x, end=' ')
print(y, end=' ')

while x + y < 1000:
    temp = x
    x = y
    y = x + temp
    print(y, end=' ')

