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

text = Text(root, bd=2, font="Tahoma 20", bg="Yellow", fg="Green", width=40)

scrollbar = Scrollbar(root, command=text.yview, orient=VERTICAL)

text['yscrollcommand'] = scrollbar.set

text.pack(side='left')
scrollbar.pack(side='left', fill=Y)

root.mainloop()