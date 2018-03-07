print('Witaj w książce kontaktów.\n')

contacts_list = []


def add_contact():
    '''
    Adds new contact to the list
    :return: list
    '''
    last_name = ''
    first_name = ''
    while len(last_name) < 1:
        last_name = input('Podaj nazwisko:\n')
    while len(first_name) < 1:
        first_name = input('Podaj imię:\n')
    age = int(input('Podaj wiek:\n'))
    contact = [last_name, first_name, age]
    contacts_list.append(contact)
    print('Kontakt dodany poprawnie\n')
    print(contacts_list, '\n')
    users_choice()
    return contacts_list


def contact_search():
    '''
    Iterates through the list and return value of contact
    and gives ability to delete
    :return: index
    '''
    name = input('Podaj szukaną frazę:\n')
    for contact in contacts_list:
        for name in contact:
            print('Kontakt znaleziony:\n', contact, '\n')
            if_delete = input('''Co chcesz zrobic z tym kontaktem?
1. Skasowac
0. Nic - wróc do głównego menu.\n''')
            if if_delete == '1':
                index = contacts_list.index(contact)
                contacts_list.pop(index)
                print('Kontakt skasowany\n')
                users_choice()
            else:
                users_choice()
        else:
            print('Nie ma takiego kontaktu. Spróbuj jeszcze raz\n')
            users_choice()


def display_contacts():
    for no, contact in enumerate(contacts_list, 1):
        print(no, contact)
    print('\n')


def users_choice():
    decision = input('''Co chcesz zrobić?
    1. Dodaj kontakt
    2. Szukaj kontaktu
    3. Wyświetl kontakty
    0. Opuść program\n
    ''')
    while not decision.isdigit():
        print('Niepoprawny wybór. Spróbuj jeszcze raz\n')
        users_choice()
    if int(decision) == 1:
        add_contact()
    elif int(decision) == 2:
        contact_search()
        users_choice()
    elif int(decision) == 3:
        display_contacts()
        users_choice()
    elif int(decision) == 0:
        exit()
    else:
        print('Niepoprawny wybór. Spróbuj jeszcze raz\n')
        users_choice()


users_choice()
