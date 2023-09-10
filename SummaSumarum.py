# gick igenom på framme

print("""
--------------------
.: SUMMA SUMMARUM :.
--------------------
Stängs vid inmatning
 av negativt heltal 
--------------------""")

i = 0
sum = 0


while (i >= 0):
    sum += i
    i = (input("Heltal: "))

    try:
        i = int(i)
    except ValueError:
        print('FEL: Ogiltigt heltal(' + str(i) + ')' )
        i = 0

print('--------------------')

print('SUMMA: ' + str(sum))