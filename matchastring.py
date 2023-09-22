s1 = ('hello man')  # input('skriv whalla:')
s2 = ('hello boy')  # input('skriv igen')
print('..............')

if len(s1) != len(s2):
    print('fellängd idiott')
    exit()
i = 0
c = 0
while i < len(s1):
    if s1[i] != s2[i]:
        c += 1
        print('ejj håå olika', i)
        print('..... ')
        print(s1)
        print(s2)
        print(' ' * i + '^')
        break
    i += 1
else:
    print('YIHOO DET MATCHAR')
