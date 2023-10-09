import json
import os

dlines = '------------------'

def cont():
    input('Press enter to\ncontinue...')

with open ('file.json') as f:
    global list
    data = json.loads(f.read())
    list = data 

def printlist():
    for i in list:
        print(f' - {i["title"]}') 

def rm():
    rm = input('title > ')
    if any(d['title'] == rm for d in list):
        for id, i in enumerate(list):
            if rm == i['title']:
                del list[id]
                print(dlines)
                print('Note deleted')
                print(dlines)
                cont()
                break
    else:
        print(dlines)
        print(f'Error: bad input ({rm})')
        print(dlines)
        cont()

def add():
    title = input('title > ') 
    descr=input('discr > ')
    list.append({'title': title,'descr': descr})
    print(dlines)
    print('Note added')
    print(dlines)
    cont()

def view():
    di = input('title > ')
    if any(d['title'] == di for d in list):
        for i in list:
            if di == i['title']:
                print(dlines)
                print(i['descr'])
                print(dlines)
                cont()
                break
    else:
        print(dlines)
        print(f'Error: bad input ({di})') 
        print(dlines)
        cont()           

d = {'add': add, 'view': view, 'rm':rm }

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('.: ALWAYSNOTE :.\n-- gold edition --\n******************')
    printlist()
    print('''------------------
view | view note
add  | add note
rm   | remove note
exit | exit program
------------------''')
    ui = input('menu > ')
    print(dlines)
    if ui in d:
        d[ui]()
    elif ui == 'exit':
        with open('file.json','w') as f:
            fl = json.dumps(list)
            f.write(fl)
        break
    else:
        print(dlines)
        print(f'Error: bad input ({ui})')
        print(dlines)
        cont()