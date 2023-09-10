print('''
*****************************
      Mathlet Calculator
-----------------------------
 add | Add two numbers
 sub | Subtract two numbers
 mul | Multiply two numbers
 div | Divide two numbers
-----------------------------''')

yataza = 0

yeeho = 0

while True:
    yataza = input('Select Yatzy > ')
    try:
        yataza = float(yataza)
        print('invalid yataza!!')
    
    except ValueError:
        yataza = yataza.upper()
        if yataza == 'ADD':
            break
        elif yataza == 'SUB':
            break
        elif yataza == 'DIV':
            break
        elif yataza == 'MUL':
            break
        else:
            print('inte räknesätt yataza')
    


while True:
    a = input('Frst num > ')
    try:
        a = float(a)
        break
    except ValueError:
        print ('invalid num')

while True:
    b = input('second num > ')
    try:
        b = float(b)
        break
    except ValueError:
        print('invalid num')

svar = 0


if yataza == 'ADD':
    svar = a + b
elif yataza == 'SUB':
    svar = a - b
elif yataza == 'DIV':
    try:
        svar = a/b
    except ZeroDivisionError:
        svar = 'NaN'
elif yataza == 'MUL':
    svar = a * b
    

print('SVARET ÄR = ' + str(svar))
