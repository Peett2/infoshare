import os
# import pdb
# pdb.set_trace()
# dane
monety = [0, 2, 1, 0.5, 0.2, 0.1]
monety_reszta = [0, 0, 0, 0, 0, 0]

banknot = 20
zakup = 8.30
reszta = banknot - zakup

# indeks do trzymania pozycji listy
indeks_mon_reszta = 0

for moneta in monety:
    if reszta >= moneta:
        # ilosc = reszta // moneta
        try:
            ilosc = reszta // moneta
            wartosc = ilosc * moneta
            reszta = reszta - wartosc
        # except ZeroDivisionError:
        #     # print('pojawił się błąd bo jest dzielenie przez 0')
        #     continue
        # except NameError:
        #     continue
        except (ZeroDivisionError, NameError) as error:
            print(error)
            continue
        wartosc = ilosc * moneta
        reszta = reszta - wartosc
        # os.path.split('/home/')

        monety_reszta[indeks_mon_reszta] = ilosc

    indeks_mon_reszta += 1

print('monety:', monety)
print("Reszta do wydania:", monety_reszta)
