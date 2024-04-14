handler = open('a.txt', 'w')
handler.write("abc 123\n890")
handler.close()

handler = open('a.txt', 'r')
print(handler.read(2))
print(handler.read())

handler.seek(0)
print(handler.read())

handler.seek(0)

for line in handler:
    print(line)

handler.close()

print("------------")

file = "b.txt"

while True:
    print("1 - Записать в файл; 2 - Прочитать файл; 0 - Выход")
    inp = input("Введите команду: ")
    if inp == "0":
        exit(0)
    elif inp == "1":
        text = input("Введите строку: ")
        handler = open(file, 'w')
        handler.write(text)
        handler.close()
    elif inp == "2":
        try:
            handler = open(file, 'r')
            print(handler.read())
            handler.close()
        except FileNotFoundError:
            print("Файла ещё не существует!")
    else:
        print("Неизвестная команда")
        