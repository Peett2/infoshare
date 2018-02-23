# ta funkcja ma zdefiniowany jeden argument domyslny imie
# jesli uzytkowniknie poda wartosci to zostanie uzyta
# domyslna wartosc - "ola"
def wypisz_imie(imie="ola"):
    imie = imie.capitalize()
    print(imie)

# uzytkownik nie musi podawac wartosci argumentu domyslnego
wypisz_imie()

# albo moze podac swoja wartosc
wypisz_imie("arek")
wypisz_imie("marta")
wypisz_imie("jola")