import csv
from pathlib import Path

file_path = Path(__file__).absolute().parent.joinpath('contacts.txt')


# define Person class
class Person:
    '''
    Class soring the contact details
    '''

    def __init__(self, last_name, first_name, age):
        self.name = last_name
        self.surname = first_name
        self.age = age


def contact_search(contacts_list):
    '''
    Iterates through the list and return value of contact
    and gives ability to delete
    :return: index
    '''
    name = input('Podaj szukaną frazę:\n')
    for contact in contacts_list:
        if name in contact:
            print('Kontakt znaleziony:\n', contact, '\n')
            if_delete = input('''Co chcesz zrobic z tym kontaktem?
1. Skasowac
0. Nic - wróc do głównego menu.\n''')
            if if_delete == '1':
                index = contacts_list.index(contact)
                contacts_list.pop(index)
                print(contacts_list)
                print('Kontakt skasowany\n')
    # else:
    #     print('Kontakt nie został znaleziony\n')
    #     users_choice()
    return contacts_list


def display_contacts(contacts_list):
    for no, contact in enumerate(contacts_list, 1):
        print(no, contact)
    print('\n')


def users_choice(store=[]):
    if not store:
        contacts_list = read_file(file_path)
        store.append(contacts_list)
    else:
        contacts_list = store
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
        add_contact(contacts_list)
        __str__(Person)
        save_file(file_path, contacts_list)
        # users_choice()
    elif int(decision) == 2:
        contacts_list = contact_search(contacts_list)
        save_file(file_path, contacts_list)
        store[0] = contacts_list
        users_choice()
    elif int(decision) == 3:
        display_contacts(contacts_list)
        users_choice()
    elif int(decision) == 0:
        exit()
    else:
        print('Niepoprawny wybór. Spróbuj jeszcze raz\n')
        users_choice()


def add_contact(contacts_list):
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
    contact = Person(last_name, first_name, age)
    contacts_list.append([contact])
    print('Kontakt dodany poprawnie\n')
    print(contacts_list, '\n')


def read_file(path):
    with open(path, 'r') as file:
        return [item for item in csv.reader(file)]


def save_file(path, contacts_list):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(contacts_list)


if __name__ == '__main__':
    users_choice()


def __str__(self):
    person = Person()
    return person
