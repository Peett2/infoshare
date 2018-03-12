# class Samochod:
#     def __init__(self, marka, model, start=False):
#         print('Wywołuję __init__')
#         self.marka = marka
#         self.model = model
#         self.uruchomiony = start
#
    # def __str__(self):
    #     return f'Samochód marki {self.marka} model {self.model}' \
    #            f' uruchomiony? {self.uruchomiony}'
#
#     def __len__(self):
#         return len(self.marka)
#
#     def uruchom_samochod(self):
#         self.uruchomiony = True
#
#     def wylacz_silnik(self):
#         self.uruchomiony = False
#
#
# if __name__ == '__main__':
#     print('Przed utworzeniem instancji')
#     golf = Samochod('Volkswagen', 'Golf')
#     print('Po utworzeniu instancji')
#     print(golf)
#     golf.uruchom_samochod()
#     print(golf)
#     megane = Samochod('Renault', 'Megane', start=True)
#     print(megane)
#     megane.wylacz_silnik()
#     print(megane)
#     print(len(megane))


class Car:
    def __init__(self, producer, model, engine=None):
        self.producer = producer
        self.model = model
        self.engine = engine

    def __str__(self):
        return f'Samochód marki {self.producer} model {self.model}' \
               f' silnik: {self.engine}'

    def __len__(self):
        return len(self.producer)

    def boost(self, amount):
        self.engine.increase_bhp(amount)


class Engine:
    def __init__(self, pojemnosc, fuel, bhp, running):
        self.pojemnosc = pojemnosc
        self.fuel = fuel
        self.bhp = bhp
        self.running = running

    def __str__(self):
        return f'Silnik o pojemności {self.pojemnosc} napędzany ' \
               f'paliwem {self.fuel} ma moc {self.bhp} a czy jest ' \
               f'uruchomiony? {self.running}'

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def increase_bhp(self, amount):
        self.bhp += amount


if __name__ == '__main__':
    v8 = Engine(5.7, 'petrol', 400, True)
    jeep = Car('Jeep', 'Cheeroke XJ', v8)
    print(jeep)
    jeep.boost(100)
    print(jeep)