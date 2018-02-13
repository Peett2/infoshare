# Narysuj piramidę Mario - jako input - wysokość piramidy
# np. piramida wysokości 3 ma wyglądać:

  #
 ###
#####

h = int(input('Podaj wysokość piramidy:\n'))

while h < 1:
    h = int(input('Raczej tak niskiej nie wybudujemy. Spróbuj jeszcze raz:\n'))

row = 1

while h >= 1:
    print(' ' * h, '#' * row)
    h -= 1
    row += 2