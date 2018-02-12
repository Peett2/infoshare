# program, ktory wypisze liczby od 0 do 20 poza liczbami podzielnymi przez 4
# continue

i=0
y=int(input('Podaj granicę ciągu:\n'))

while i <= y:
    if i % 4:
        print(i)
        i+=1
    else:
        i+=1
        continue
