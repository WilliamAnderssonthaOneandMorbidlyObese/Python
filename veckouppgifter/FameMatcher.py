print("""
.: FAME MATCHER: .
------------------
Search of the day!
female, brown, brown
------------------""")
gender = input('Gender: ')
hair = input('Hair Color: ')
eye = input('Eye Color: ')
print('------------------')
nomatch = 'NO MATCH :('

if (gender.upper()) == 'MALE':
    if (hair.upper()) == 'BROWN':
        if (eye.upper()) == 'BROWN':
            print('MATCH: Daniel Radcliffe')
        elif (eye.upper()) == 'BLUE':
            print('MATCH: Ryan Gosling, Robert Pattinson, Willem Dafoe')

        else:
            print(nomatch)

    elif (hair.upper()) == 'RED':
        if (eye.upper()) == 'BLUE':
            print('MATCH: Rupert Grint')
        else:
            print(nomatch)
    else:
        print(nomatch)
    

elif (gender.upper()) =='FEMALE':
    if (hair.upper()) == 'BROWN':
        if (eye.upper()) =='BROWN':
            print('MATCH: Emma Watson, Selena Gomez')
        else:
            print(nomatch)
    elif (hair.upper()) == 'BLONDE':
        if(eye.upper()) == 'BLUE':
            print('MATCH: Margot Robbie, Meryl Streep')
        else:
            print(nomatch)
    else:
        print(nomatch)
else:
    print(nomatch)