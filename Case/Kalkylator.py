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
# ta input av användare
while yataza != ('DIV','SUB','ADD','MUL'):
    yataza = input('Select Yatzy > ')
    try:
        yataza = float(yataza)
        print('invalid yataza!!')
    
    except ValueError:
        yataza = yataza.upper()
        if yataza == 'ADD':
            print('ofan')
    # try:
    #     yataza = str(yataza)
    #     yataza = yataza.upper()
    #     if yataza == 'ADD':
    #         yataza = 'ADD'
    #         print('hej kom och hjälp mig!!')
    #     elif yataza == 'SUB':
    #         yataza = 'SUB'
    #     elif yataza == 'MUL':
    #         yataza = 'MUL'
    #     elif yataza == 'DIV':
    #         yataza = 'DIV'
    # except ValueError:
    #     print('invalid yatza')
# kolla om det är div hej hå
# ta mer input

# gör om till float

# skriv ut summan 
 
#  fixa valueerror och zerodiv error