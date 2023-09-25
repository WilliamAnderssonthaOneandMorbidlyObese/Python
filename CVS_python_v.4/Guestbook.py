import os
import json

# LÄS IN GÄSTBOK FRÅN FIL
f = open('guestbook.json')
guestbook = f.read()
guestbook = json.loads(guestbook)
f.close()

while True:  # bryts när användaren matar in 'exit'

    # RENSA TERMINALFÖNSTER
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

    # SKRIV UT HEADER
    print('.: The Guestbook :.')
    print(19 * '-')

    # SKRIV UT GÄSTBOKENS INLÄGG
    for entry in guestbook:
        print(entry)
        print(19 * '-')

    # HÄMTA INLÄGG FRÅN ANVÄNDARE
    entry = input('NYTT INLÄGG > ')

    # BRYT LOOPEN OM ANVÄNDAREN MATAR IN 'exit'
    if entry.lower() == 'exit':
        break

    # LÄGG TILL INLÄGG TILL GÄSTBOK
    guestbook.append(entry)

# SKRIV GÄSTBOK TILL FIL
f = open('guestbook.json', 'w')
guestbook = json.dumps(guestbook)
f.write(guestbook)
f.close()
