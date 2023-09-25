import json

f = open('data.json')
data = f.read()
data = json.loads(data)
f.close()

print(type(data))
print(data[2])

e = 'yayy'

data.append({'name': 'hoppa', 'gör': 'spring'})

print(data)

f = open('data.json', 'w')
data = json.dumps(data)
f.write(data)
f.close()

input('')
