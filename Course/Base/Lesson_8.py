i = 0
while i < 10:
    i += 1 #i = i + 1
    print("Hello World!")
print("Цикл завершён, i =", i)

print("----------")

i = 0
while i < 10:
    i += 1
    print(i)

print("----------")

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    if i == 8:
        break
    print(i)
print("Цикл завершён, i =", i)

print("----------")
s = 0
x = 1
to = 10
while x <= to:
    s += x
    x += 1
print("Сумма чисел от 1 до", to, "равна", s)

while True:
    code = input("Введите 0 для выхода: ")
    if code == "0":
        break

exit(0)
print("----------")
i = 0
while True:
    i += 1
    print(i)