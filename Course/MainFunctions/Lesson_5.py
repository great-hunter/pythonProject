d = {'name': 'Alex', 'age': 35}
print(d)
d.setdefault('isWorking', True)
print(d)
print(d.get('age'))
d.pop('name')
print(d)

keys = list(d.keys())
print(keys)
print(keys[0])

print("--------")

values = list(d.values())
print(values)
print(values[0])

d['age'] = 40
d['isMale'] = True
print(d)

d.clear()
print(d)