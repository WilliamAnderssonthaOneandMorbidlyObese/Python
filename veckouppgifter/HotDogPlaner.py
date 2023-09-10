import math

villha = 'Hur många vill ha: '
vanliga = ' vanliga krovar? --> '
vegan = ' vegan korvar? --> '



print('⠀')
print(' .: hot dog planer :. '.upper())
print('-------------------------')
print(villha)

while True:
    meatsqr = int(input( '2' + vanliga ))
    if meatsqr < 0:  
        print ('Skriv ett antal större eller lika med 0!')
    else:
        break

while True:
    meatcub = int(input( '3' + vanliga))

    if meatcub < 0:
        print('Skriv ett antal större eller lika med 0!')
    else:
        break    

while True:
    vegansqr = int(input( '2' + vegan))

    if vegansqr < 0:
        print('Skriv ett antal större eller lika med 0!')
    else:
        break

while True:
    vegancub = int(input( '3' + vegan))

    if vegancub < 0:
        print('Skriv ett antal större eller lika med 0!')
    else:
        break

meatcmb = ((meatcub * 3) + (meatsqr * 2)) / 8
vegancmb = ((vegansqr * 2) + (vegancub * 3)) / 4

meatamt = (math.ceil(meatcmb))
veganamt = (math.ceil(vegancmb))

festis = meatcub + meatsqr + vegancub + vegansqr

meatkr = (meatamt * 20.95)
vegankr = (veganamt * 34.95)
festkr = (festis * 13.95)

print('-------------------------')

print('Det behövs ' + str(meatamt) + ' packet vanlig korv. För ' + str(round(meatkr,1)) + 'kr')
print('Det behövs ' + str(veganamt) + ' packet vegankorv. För ' + str(round(vegankr,1)) +'kr')
print('Och ' + str(festis) + ' festis för ' + str(round(festkr,1)) + 'kr')

print('-------------------------')

total = round(meatkr + vegankr + festkr,1)
print('Totalt blir det ' + str(total) +('kr') )
print('⠀')
