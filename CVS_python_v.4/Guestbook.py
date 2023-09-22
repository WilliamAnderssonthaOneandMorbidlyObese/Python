import os
import json

f = open('guestbook.json')
guestbook = f.read()
guestbook = json.loads(guestbook)
f.close()

guestbook = ['Hej', 'Crille was here', 'Hejdå']

while True:
    os.system('cls')
    print('\n.: THE GUESTBOOK :.\n---------')
    for entry in guestbook:
        print(entry)
        print('----------')
    entry = input('NYTT INLÄGG--')

    if entry == 'exit':
        break

    guestbook.append(entry)
    f.open('guestbook.json', 'w')
    guestbook = json.dumps(guestbook)
    f.write(guestbook)
    f.close
with open("filename.dat") as file:
    print(file)
