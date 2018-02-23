# Napisz program, który będzie bazą kontaktów, program ma pytać
# użytkownika, co chce zrobić, dając mu minimum te opcje: dodanie imienia,
# usuniecie imienia, sprawdzenie czy imię jest w bazie, usunięcie imienia,
# sprawdzenie ilości imion w bazie oraz zakończenie programu.
# Jeśli czujesz się pewniej to postaraj się aby użytkownik mógł podać więcej
# szczegółów np. nazwisko, nr telefonu, adres itp.
# Program ten będziemy pomału rozbudowywać, w kolejnych tygodniach
# Oczywiście piszemy już „Czysty kod” stosując się do konwencji
# Python’owych: piszemy docstringi, właściwe i znaczące nazwy zmiennych
# oraz funkcji. I jeśli damy radę to możemy postarać się stworzyć moduły z
# oddzielnymi funkcjonalnościami.

# formatowanie = (name=None, surname= None, phone=None, addressn=None)
def contact_input():
    # contact = [name='None', surname='None', phone='None', address='None']
    name = input('Input name:\n')
    # return name
    print(name)
    surname = input('Input surname:\n')
    # return surname
    print(surname)
    phone = input('Input phone:\n')
    # return phone
    print(phone)
    address = input('Input address:\n')
    # return address
    print(address)
    contact = [name, surname, phone , address]
    print(contact)


contact_input()
# zdefiniuj listę

# przypisz jej zmienne

# argument domyslny jest typem referencyjnym
def dodaj_imie(imie, imiona=[]):
    imiona.append(imie)
    return imiona


# jesli nie podamy argumentu domyslnego
# to Python utworzy typ referencyjny tylko przy pierwszym
# wywolaniu funkcji
lista_imion = dodaj_imie("Ola")
print(lista_imion)

# drugie wywolanie i myslimy ze dodajemy imie do nowej listy
# a okazuje sie ze to jest ta sama lista !
lista_imion2 = dodaj_imie("Ala")
print(lista_imion2)

lista_imion3 = dodaj_imie("Piotrek")
print(lista_imion3)

# zwizualizuj kod na pythontutor.com aby zobaczyc
# co sie dzieje
