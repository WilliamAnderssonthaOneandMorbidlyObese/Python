'''head notes:
Du har inte fixar en snygg ui med mer än 10 items i check och delete
ditt dumma pap loadar man två gånger i rad dubblar man listan'''


# import libraries
import os
import json

ui_width = 36
dotted_line = '*'*ui_width
dashed_line = '-'*ui_width

# Define a function to print the main user interface


def main_ui():
    print(dotted_line)
    print('Todoify'.center(ui_width))
    print(f'''{dashed_line}
list   | List todos
add    | Add todo
check  | Check todo
delete | Delete todo
{dashed_line}
save   | Save todos to file
load   | Load todos from file
{dashed_line}''')

# Define a function to print the todos with their indices and statuses


def printtodos():
    print(dashed_line)
    # Loop through the todolist and enumerate each item
    for id, items in enumerate(todolist):
        if select == 'list':
            if items['check'] == False:
                print(f'[ ] {items["todo"]}')
            else:
                print(f'[X] {items["todo"]}')
        else:
            if items['check'] == False:
                print(f'{str(id).ljust(2)}| [ ] {items["todo"]}')
            else:
                print(f'{str(id).ljust(2)}| [X] {items["todo"]}')
    print(dashed_line)


def cont(message):
    if message != '':
        print(dashed_line)
        if message == 'added':
            print('\nSUCCESS: Todo added\n')
        elif message == 'checked':
            print('\nSUCCESS: Unchecked -> Checked\n')
        elif message == 'unchecked':
            print('\nSUCCESS: Checked -> Unchecked\n')
        elif message == 'delete':
            print('\nSUCCESS: Todo deleted\n')
        elif message == 'save':
            print(f'\nSUCCESS: Todos saved to {file.name}\n')
        elif message == 'load':
            print(f'\nSUCCESS: Todos loaded from {file.name}\n')
    input('Press enter to continue...')

# Define a function to handle unknown commands


def selecterr():
    print(dashed_line)
    print(f'''
ERROR: Unknown command '{select}'
''')
    cont(message='')


def indexerr():
    print(dashed_line)
    print(f'''
ERROR: {todoindex} is not a valid index.
''')
    cont(message='')


# Initialize an empty list to store the todos
todolist = []


# Define a function to list the todos
def listt():
    printtodos()
    cont(message='')

# Define a function to add a todo


def add():
    print(dashed_line)
    todo = input('Todo description > ')
    todolist.append({'check': False, 'todo': todo})
    cont(message='added')

# Define a function to check or uncheck a todo


def check():
    global todoindex
    printtodos()
    todoindex = input('Todo index > ')
    try:
        todoindex = int(todoindex)
    except (ValueError, TypeError):
        indexerr()
        return

    if todoindex >= 0 and todoindex < len(todolist):
        if todolist[todoindex]['check'] == False:
            todolist[todoindex]['check'] = True
            cont(message='checked')
        else:
            todolist[todoindex]['check'] = False
            cont(message='unchecked')
    else:
        indexerr()

# Define a function to delete a todo


def delete():
    global todoindex
    printtodos()
    todoindex = input('Todo index > ')
    try:
        todoindex = int(todoindex)
    except (ValueError, TypeError):
        indexerr()
        return

    if todoindex >= 0 and todoindex < len(todolist):
        del todolist[todoindex]
        cont(message='delete')
    else:
        indexerr()


def save():
    global file
    with open('TodoData.json', 'w') as file:
        data = json.dumps(todolist)
        file.write(data)
        cont(message='save')


def load():
    global todolist
    global file
    with open('TodoData.json') as file:
        data = json.loads(file.read())
        todolist = data + todolist
        cont(message='load')


# Define a dictionary that maps each command to its corresponding function
selection = {'add': add, 'list': listt, 'check': check,
             'delete': delete, 'save': save, 'load': load}


# Print the main user interface in a while loop
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    main_ui()
    select = input('Selection > ')
    if select in selection:
        selection[select]()
    else:
        selecterr()
