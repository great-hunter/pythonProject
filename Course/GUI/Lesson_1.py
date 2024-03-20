from tkinter import *

root = Tk()
root.title("Окно программы")
root.resizable(False, False)

w = 800
h = 600
ws = root.winfo_screenwidth()
wh = root.winfo_screenheight()

x = int(ws / 2 - w / 2)
y = int(wh / 2 - h / 2)

#root.geometry("800x600+700+400")

root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

root.mainloop()