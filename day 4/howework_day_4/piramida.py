# Narysuj piramidę Mario - jako input - wysokość piramidy
# np. piramida wysokości 3 ma wyglądać:

  #
 ###
#####

hight = int(input('Podaj wysokość piramidy:\n'))

while hight < 1:
    hight = int(input('Raczej tak niskiej nie wybudujemy. Spróbuj jeszcze raz:\n'))

# narysuj '   ' oraz 1x'#'
# dodaj 1x' ' do poprzedniego i 2x'#'

spaces_no = 1
hashes_no = 0
rows = 1
row_no = 1

while rows <= hight:
    while spaces_no <= row_no:
        print(' ')
        spaces_no += 1
    while hashes_no+1
    print('\n')
    rows += 1
    # print('#')
