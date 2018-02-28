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

print('Witaj w książce kontaktów.\n')

contacts_list = []

# name = str

def add_contact():
    '''
    Adds new contact to the list
    :return: list
    '''
    name = input('Input name:\n')
    name.capitalize()
    contacts_list.append(name)
    return contacts_list


def contact_search():
    '''
    Iterates through the list and return value of contact and finds the index
    :return: index
    '''
    name = input('Podaj szukaną frazę:\n')
    # idx = name.index()
    if name in contacts_list:

        print('Kontakt znaleziony:\n', name, '\n', 'jego index to:')
    else:
        print('Nie ma takiego kontaktu. Spróbuj jeszcze raz\n')
        contact_search()


def display_contacts():
    for no, contact in enumerate(contacts_list, 1):
        print(no, contact)
    print('\n')


def users_choice():
    decision = int(input('''Co chcesz zrobić?
    1. Dodaj kontakt
    2. Szukaj kontaktu
    3. Wyświetl kontakty
    0. Opuść program\n
    '''))
    if decision == 1:
        add_contact()
        print(contacts_list, '\n')
        users_choice()
    elif decision == 2:
        contact_search()
        users_choice()
    elif decision == 3:
        display_contacts()
        users_choice()
    elif decision == 0:
        exit()
    else:
        users_choice()


users_choice()