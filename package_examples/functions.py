def hello(username):
    '''
    Returns uppercased username\n
    :param username: string\n
    :return: str.upper()
    '''
    name = username.upper()
    print('locals', locals())
    return name


name = 'ania'
lastname = 'Kowalska'

if __name__ == '__main__':
    print(hello(name))
    print('globals', globals())
