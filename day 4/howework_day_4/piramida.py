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

no_spaces = 1
no_hashes = 0
rows = 1
row_no = 1

while rows <= hight:
    while no_spaces <= row_no:
        print(' ')
        no_spaces += 1

    # print('#')
    # rows += 1
    print('\n')