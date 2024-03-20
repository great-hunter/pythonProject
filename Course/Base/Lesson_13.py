mydict = dict()
print(mydict)
mydict = {'Name' : 'John', 'Age' : 35}
print(mydict)

mydict = dict(Name='John', Age=35, isMale=True)
print(mydict)

print(mydict['Age'])

print('---------')

for key in mydict:
    print(key, '=', mydict[key])

mytuple = ('Name', 'Age', 'isMale')
for key in mytuple:
    print(key, '=', mydict[key])

print('---------')
mydict = {i * 2 : i for i in range(1, 10)}
print(mydict[2])
mydict = {str(i * 2) : i for i in range(1, 10)}
print(mydict)