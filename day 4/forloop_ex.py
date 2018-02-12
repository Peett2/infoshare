# @TODO input: start, stop, *krok* (**user podaje <start,stop,krak>**)
# @TODO **funkcja split() z delimiterem**
# @TODO wykorzystujac pętlę
# @TODO ile jest liczb przystych ile jest liczb nieparzystych w zbiorze
# @TODO od start do stop włącznie

x=input('Podaj dane w formacie: <start,stop,krok>:\n')

start,stop,krok = x.split(',')

print('Podane dane to:\n', start, stop, krok)

start = int(start)
stop = int(stop)
krok = int(krok)

evens = 0
odds = 0

for idx in range(start, stop+1, krok):
    if idx % 2:
        evens += 1
        print(idx,';',evens,'evens')
    elif idx + 1 % 2:
        odds += 1
        print(idx,';',odds,'odds')

print('odds: ',odds)
print('evens: ',evens)