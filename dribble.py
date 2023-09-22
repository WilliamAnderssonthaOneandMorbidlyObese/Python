import os

# FUNKAR EJ FIXA OM DU VILL

h = 'tensta'  # input('LAG HEM:')
a = 'uppsala'  # input('LAG BORT:')
hS = 0
aS = 0


def ui():
    print('''
    .-----------------------------.
    |        BASKET SWEDEN        |
    |*****************************|''')
    print('|', h.center(12), '|', a.center(12),
          '|')  # ska stå rätt kunde in bry mig
    print('''|-----------------------------|
    | ''', hS, ''' | ''', aS, ''' |
    |*****************************|
    | H2 | 2 points to Västerås   |
    | H3 | 3 points to Västerås   |
    | A2 | 2 points to Stockholm  | 
    | A3 | 3 points to Stockholm  |
    |-----------------------------|
    | EX | Exit program
    |-----------------------------|''')


while True:
    os.system('cls')
    ui()

    s = input('gogog > ')
    if s == 'H2':
        hS += 2
    elif s == 'H3':
        hS += 3
    elif s == 'A2':
        aS += 2
    elif s == 'A3':
        aS += 3
    elif s == 'EXIT':
        break
