print(f'''SomethingCSV
--------------''')
f = open('database.csv')
csv = f.read()

rows = csv.split('\n')
del rows[0]
del rows[-1]

prefixes = ["ID:", "FORENAME:", "SURNAME:", "GENDER:", "AGE:"]

for row in rows:
    columns = row.split(',')
    for i in range(len(columns)):
        print(f"{prefixes[i].ljust(11)}{columns[i]}")
    print("---")
 # tage rökte på som satan
