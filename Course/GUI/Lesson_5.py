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

text = Text(root, bd=2, font="Tahoma 20", bg="Yellow", fg="Green", width=10, height=4, padx=10, pady=20)

text.insert(END, "Hello\nABC")

print(text.get("1.0", END))

text.pack()

root.mainloop()