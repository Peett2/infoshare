# @TODO input: start, stop, *krok* (**user podaje <start,stop,krak>**)
# @TODO **funkcja split() z delimiterem**
# @TODO wykorzystujac pętlę
# @TODO ile jest liczb przystych ile jest liczb nieparzystych w zbiorze
# @TODO od start do stop włącznie

start= int(input('Podaj start\n'))
stop= int(input('Podaj stop\n'))
krok= int(input('Podaj krok\n'))
odds=0
for idx in range(start,stop+1,krok):
    if idx % 2:
        odds+=1

print(odds)