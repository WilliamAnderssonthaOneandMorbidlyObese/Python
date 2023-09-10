import random
import time

print('''
---------------
.:  12 dices  :.
----------------
 Press enter to 
    throw!    
----------------
TOTAL | PREVIOUS''')

i = 0
sump = 0
sumd = 0

print('''****************
      YOU       ''')

while sump < 12:
    input(sump)
    d = random.randint(1,6)
    sump += d
    print("             " + '['+ str(d)+ ']')
print (str(sump))


print('''****************
      DEALER       ''')

while sumd < 12:
    print(sumd)
    time.sleep(1)
    d = random.randint(1, 6)
    sumd += d
    print("             " + '[' + str(d) + ']')
print(str(sumd))

print('''****************
        RESULT''')

print('player:', sump)
print('dealer:', sumd)
print('**************')

if sumd == sump:
    print('draw')
elif sump < sumd:
    print('dealer win')
else:
    print('player win')
