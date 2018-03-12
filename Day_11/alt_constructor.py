class Zwierze:
    def __init__(self, imie):
        print('init zwierze')
        self.imie = imie

    def mowi(self):
        print('zwierze nie mowi')

    def __str__(self):
        return str(self.imie).capitalize()


class Kon(Zwierze):
    def __init__(self, imie):
        print('init koń')
        Zwierze.__init__(self, imie)

    def mowi(self):
        print('hej jestem koń')

    def skacz(self):
        print('koń skacze')


class Osiol(Zwierze):
    def __init__(self, imie):
        print('init osiol')
        Zwierze.imie = imie

    def mowi(self):
        print('osiol mowi')

    def biegnij(self):
        print('osioł nie biega')


class Mul(Osiol, Kon):
    def __init__(self, imie):
        print('init mul')
        # super().__init__(imie)
        Osiol.__init__(self, imie)
        Kon.__init__(self, imie)

    def mowi(self):
        print('mowie jestem mułem')

    def biegne(self):
        print('muły nie biegaja')


print('\nZwierzak: ------------------')
# tworzymy instancje Zwierze
animal1 = Zwierze('zwierzak')
print(animal1)
animal1.mowi()

print('\nKoń: ------------------')
# tworzymy instancje Kon
kon1 = Kon('Kary')
print(kon1)
# jak widzimy kon korzysta z wlasnej implementacji
kon1.mowi()
kon1.skacz()

print('\nOsioł: ------------------')
osiol1 = Osiol('donkey kong')
osiol1.mowi()
osiol1.biegnij()

print('\nMuł: ------------------')
mul1 = Mul('Mułek')
mul1.mowi()
mul1.skacz()
mul1.biegnij()
