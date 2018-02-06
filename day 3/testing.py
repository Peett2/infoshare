aa = str(input('Jak masz na imię?\n'))

if aa.endswith('a') and aa!='Jan Maria':
    print('Cześć koleżanko',aa.capitalize())
else:
    print('Cześć Kolego',aa.capitalize())