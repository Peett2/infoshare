import pprint


class Contact:
    contacts_no = 0
    last_id = 0

    def __init__(self, name, lastname):
        Contact.last_id += 1
        self.id = Contact.contacts_no
        self.name = name
        self.lastname = lastname
        Contact.contacts_no += 1

    def full_name(self):
        return f'{self.name} {self.lastname}'

    def __str__(self):
        return f'Id: {self.id} Name: {self.name} Lastname: {self.lastname}'

    def __repr__(self):
        return f'Contacts({self.name}, {self.lastname})'

    def __del__(self):
        # print('called')
        Contact.contacts_no -= 1


class Phonebook:
    def __init__(self):
        self.__data = dict()

    def __len__(self):
        return len(self.__data)

    def __str__(self):
        elements = [f'{k} -> {v}' for k, v in self.__data.items()]
        # elements = []
        # for k, v in self.__data.items():
        #     text = f'{k} -> {v}'
        #     elements.append(text)
        elements_with_new_lines = '\n'.join(elements)
        return elements_with_new_lines

    def __getitem__(self, item):
        #     phonebook[4] -> data[4]
        return self.__data[item]

    def __delitem__(self, key):
        return self.__data.__delitem__(key)

    def add_contact(self, contact):
        self.__data[contact.id] = contact


if __name__ == '__main__':
    from pprint import pprint

    c = Contact('Jan', 'Kowalski')
    c2 = Contact('Adam', 'Nowak')
    print(c)
    print(c2)
    contacts = [c, c2, Contact('Adam', 'Opania')]
    pprint(contacts)
    del contacts[1]
    pprint(contacts)
    print(Contact.contacts_no)

    phonebook = Phonebook()
    phonebook.add_contact(c)
    phonebook.add_contact(c2)
    print(phonebook)
    print(phonebook[0])
    print(phonebook[1])
