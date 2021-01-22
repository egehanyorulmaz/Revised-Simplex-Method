from tkinter import *
window = Tk()
window.title("Test")
window.geometry("400x200")
L1 = Label(window, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(window, bd =5)
E1.pack(side = RIGHT)
window.mainloop()
