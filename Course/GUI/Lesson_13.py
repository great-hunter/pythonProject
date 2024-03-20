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

label1 = Label(root, text="Метка 1", font="Tahoma 20", bg="red")
label2 = Label(root, text="Метка 2", font="Tahoma 20", bg="green")
label3 = Label(root, text="Метка 3", font="Tahoma 20", bg="blue")
label4 = Label(root, text="Метка 4", font="Tahoma 20", bg="#9a3")
label5 = Label(root, text="Метка 5", font="Tahoma 20", bg="#777")

label1.grid(row=0, column=0, padx=10, pady=20)
label2.grid(row=0, column=1, ipadx=10, ipady=20)
label3.grid(row=1, column=0, columnspan=2, pady=20, ipadx=40)
label4.grid(row=2, column=0, rowspan=2, sticky="w")
label5.grid(row=2, column=1, sticky="nw")
Label(root, text="Метка 6", font="Tahoma 20", bg="#abf").grid(row=3, column=1, sticky="se")

root.mainloop()