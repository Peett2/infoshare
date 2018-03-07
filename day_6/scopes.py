name = 'Ola'


def hello(username):
    '''
    Returns uppercased username\n
    :param username: string\n
    :return: str.upper()
    '''
    name = username.upper()
    return name


data = input('Podaj imie:\n')
uppercased = hello(data)
print(uppercased)
print(name)
