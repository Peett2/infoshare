class Person:
    def __init__(self, imie='', nazwisko='', ulica='', nr='', miasto='',
                 miasto_gminne='', kod_pocztowy=''):
        self.imie = imie
        self.nazwisko = nazwisko
        self.ulica = ulica
        self.nr = nr
        self.miasto = miasto
        self.miasto_gminne = miasto_gminne
        self.kod_pocztowy = kod_pocztowy
        self.__adres = ''

    def __str__(self):
        return f'{self.imie} {self.nazwisko} {self.ulica} {self.nr} {self.miasto} {self.miasto_gminne} {self.kod_pocztowy}'

    @property
    def adres(self):
        if self.ulica:  # != ''
            return f'{self.ulica} {self.nr}, {self.kod_pocztowy} {self.miasto_gminne}'
        else:
            return f'{self.miasto} {self.nr}, {self.kod_pocztowy} {self.miasto_gminne}'


# @TODO napisać setter

# @adres.setter:
# def address(self, ulica, nr, kod_pocztowy, miasto_gminne):
#     self.address()


if __name__ == '__main__':
    jan = Person('Jan', 'Kowalski', 'Lea', '6', 'Krakow', 'Krakow', '30-415')
    adam = Person('Adam', 'Nowak', nr='144', miasto='Wies',
                  miasto_gminne='Miasto', kod_pocztowy='30-415')

print(jan)
print(adam)
print(adam.adres)
print(jan.adres)
