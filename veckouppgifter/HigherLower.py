import random

print('''
.: THE HIGHER LOWER GAME :.
---------------------------
Welcome to The Higher Lower
Game. I  will  randomise  a
number between  0  and  99.
Can you guess it?
---------------------------''')

rn = random.randint(0,99)
g = 0
gs = 0

while g != rn:
    if gs == 0:
        g = input('YOUR NUMBER: ')
        gs += 1
    else:
        g = input('TRY AGAIN: ')
    try:
        g = int(g)
        if g < rn:
                gs += 1
                print('HIGHER')
        elif g > rn:
                gs += 1
                print('LOWER')
        elif g == rn:
            print('''---------------------------
''' + str(rn) +''' is correct!
It took you ''' + str(gs)+''' guesses.
Good job!''')
    
    except ValueError:
        print('ERROR: not an int')
        
        