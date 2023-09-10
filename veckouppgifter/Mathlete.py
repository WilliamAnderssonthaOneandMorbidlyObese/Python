print('''.: MATHLETE v2.0 :.
-------------------''')

sum = 0
num = ''
ct = 0

while True:
    num = input('> ')
    if num.upper() == 'EXIT':
        break
    try:
        num = int(num)
        sum += num
        ct += 1
    except ValueError:
        print('ERROR: Invalid number')

try:
    mn = sum / ct
except ZeroDivisionError:
    mn = 'NaN'
    
print('''-------------------
Cardinality: ''' + str(ct)+
'''
Sum:         ''' + str(sum) +
'''
Mean value:  ''' + str(mn))
