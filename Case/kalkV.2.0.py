print('''
*****************************
      Mathlet Calculator
-----------------------------
 add | Add two numbers
 sub | Subtract two numbers
 mul | Multiply two numbers
 div | Divide two numbers
-----------------------------''')
operation = 0
result = 0

# while True:
#     operation = input('Select Operation > ')
#     try:
#         operation = float(operation)
#         print('ERROR: Not an Operation')

#     except ValueError:
#         operation = operation.upper()
#         if operation == 'ADD':
#             break
#         elif operation == 'SUB':
#             break
#         elif operation == 'DIV':
#             break
#         elif operation == 'MUL':
#             break
#         else:
#             print('ERROR: Not an Operation')

while operation != (('ADD'), ('SUB'), ('DIV'), ('MUL')):
    operation = input('Select Operation > ')
    operation = operation.upper()
    if operation != 'ADD':
        print('ERROR: Not a Operation')

print('-----------------------------')
while True:
    num1 = input('First Number > ')
    try:
        num1 = float(num1)
        break
    except ValueError:
        print ('ERROR: Invalid Number')

while True:
    num2 = input('Second Number > ')
    try:
        num2 = float(num2)
        break
    except ValueError:
        print('ERROR: Invalid Number')
print('-----------------------------')
if operation == 'ADD':
    result = num1 + num2
    operation ='+'
elif operation == 'SUB':
    result = num1 - num2
    operation ='-'
elif operation == 'DIV':
    try:
        result = num1/num2
        operation = '/'
    except ZeroDivisionError:
        result = 'NaN'
        operation = '/'
elif operation == 'MUL':
    result = num1 * num2
    operation = '*'
    
print(str(num1)+(' ')+str(operation)+(' ')+str(num2)+(' = ')+str(result))

print('Result: '+str(result))

print('*****************************')