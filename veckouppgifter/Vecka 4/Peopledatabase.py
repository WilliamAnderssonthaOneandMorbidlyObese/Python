
import os

with open ('database.csv') as f:
    data = f.read()

datarows = data.split('\n')

del datarows[-1]

def printinfoid():
    info = datarows[0].split(',')
    for id, i in enumerate(info):
        print(f'{i}: {columns[id]}')
    print('----------------------')

def printinfo():
  print(*columns, sep = ', ')

def get_id():
    global columns
    id = input('| ID > ')
    print('----------------------')
    for row in datarows:
        columns = row.split(',')
        if columns[0] == id:
            printinfoid()
            break

def get_f():
    global columns
    forename = input('| FORNAME > ')
    print('----------------------')
    for row in datarows:
        columns = row.split(',')
        if columns[1] == forename:
            printinfo()

def get_s():
    global columns
    surname = input('| SURNAME > ')
    print('----------------------')
    for row in datarows:
        columns = row.split(',')
        if columns[2] == surname:
            printinfo()

options = {'get_id': get_id, 'scan_f': get_f, 'scan_s': get_s}

while True:
    os.system( 'cls' if os.name == 'nt' else 'clear')
    print('''.: PEOPLES DATABASE: .
----------------------
get_id | Get person by ID
scan_f | List people by FORENAME
scan_s | List people by SURNAME
exit   | Exit program
----------------------''')
    select = input('| menu > ')
    if select in options:
        options[select]()
        input('Enter to continue...')
    elif select == 'exit':
        break
    else:
        print('ERROR: BAD INPUT')
        input()