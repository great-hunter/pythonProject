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

data = ["Яблоки", "Апельсины", "Лимоны"]
list = Listbox(root, font="Tahoma 20", width=20, height=4, selectmode=MULTIPLE)

for d in data:
    list.insert(END, d)

list.selection_set(1, 2)
print(list.selection_get())

indexes = list.curselection()
print(indexes)
for index in indexes:
    print(data[index])

list.pack()


root.mainloop()