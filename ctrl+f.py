a = input('TEXT: ')
b = input('BOKSTAV: ')

c = 0

print('----')


for i in a:
    if b.lower() == i.lower():
        c += 1

print('Bokstaven', b, 'förekomer', c, 'gånger i texten!!')
