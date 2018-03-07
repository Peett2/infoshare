# raises exception
# with open('non-existing.txt', 'r') as plik:
#     print(plik)
#     print(plik.read())

# creates a file if needed
# with open('non-existing.txt', 'w') as plik:
#     print(plik)


# creates a file if needed
# with open('non-existing.txt', 'a') as plik:
#     print(plik)

# raises exception
with open('non-existing.txt', 'r+') as plik:
    print(plik)