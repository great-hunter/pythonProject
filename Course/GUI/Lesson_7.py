from tkinter import *

def setwindow(root):
    root.title("Окно программы")
    root.resizable(False, False)

    w = 800
    h = 600
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

root = Tk()
setwindow(root)

label = Label(root, text="Ваш любимый цвет", font="Tahoma 20")

choice1 = StringVar()
r1 = Radiobutton(root, text="Красный", font="Tahoma 20", variable=choice1, value="red")
r2 = Radiobutton(root, text="Зелёный", font="Tahoma 20", variable=choice1, value="green")
r3 = Radiobutton(root, text="Синий", font="Tahoma 20", variable=choice1, value="blue")

choice1.set("green")

print(choice1.get())

choice2 = IntVar()
r4 = Radiobutton(root, text="Красный", font="Tahoma 20", variable=choice2, value=1)
r5 = Radiobutton(root, text="Зелёный", font="Tahoma 20", variable=choice2, value=2)
r6 = Radiobutton(root, text="Синий", font="Tahoma 20", variable=choice2, value=3)

choice2.set(2)

label.pack()
r1.pack()
r2.pack()
r3.pack()
r4.pack()
r5.pack()
r6.pack()

root.mainloop()