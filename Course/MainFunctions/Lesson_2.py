s1 = "str_1"
print(len(s1))
print(s1[1])
print(s1[-1])
print(s1[-2])
print(s1[1:3])

s1 = "abc\\nxyz"
s2 = r"abc\nxyzx"
print(s1)
print(s2)

print("------")

s1 = "hello"
s2 = s1 * 3
print(s1)
print(s2)

print(s1.find("l"))
print(s1.find("l", 3))

print("593".isdigit())
print(s1.isalpha())
print(s1.upper())
print(s1.lower())

print("------")

print(ord("a"))
print(chr(98))

s1 = "          hello           "
print(s1)
print(s1.strip())

print("------")

s1 = "Здравствуйте, {0}. Вам {1} лет!"
print(s1.format('Alex', 30))

s1 = "Здравствуйте, {name}. Вам {age} лет!"
print(s1.format(name='Alex', age=30))

data = ('Alex', 30)
s1 = "Здравствуйте, {0[0]}. Вам {0[1]} лет!"
print(s1.format(data))

s1 = "int: {0:d}; bin: {0:b}"
print(s1.format(5))

s1 = "Round (150 / 47): {0:.3}"
print(s1.format(150 / 47))