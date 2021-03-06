import tkinter as tk
from tkinter import *
import string_to_txt

def click():
    entered_objective = L1Entry.get()
    entered_objective_string = L3Entry.get()
    entered_variables = L5Entry.get()
    entered_constraints = L7Entry.get()

    string_to_txt.save_as_JSON(entered_objective, entered_variables, entered_objective_string, entered_constraints)

window = tk.Tk()
window.title("Revised Simplex Method")
window.configure(background="white")

window.geometry("500x300")
L0 = Label(window, text="", bg="white").grid(row=0, column=0, sticky=W)

L1 = Label(window, text="Objective (max or min):", bg="white").grid(row=1, column=0, sticky=W)
L1Entry = Entry (window, width=20, bg="white")
L1Entry.grid(row=1, column=2, sticky=W)

L2 = Label(window, text="", bg="white").grid(row=2, column=0, sticky=W)

L3 = Label(window, text="Objective string:\n(ex: 2*x1-3*x2+5*x3)", bg="white").grid(row=3, column=0, sticky=W)
L3Entry = Entry (window, width=20, bg="white")
L3Entry.grid(row=3, column=2, sticky=W)

L4 = Label(window, text="", bg="white").grid(row=4, column=0, sticky=W)

L5 = Label(window, text="variable list (ex: x1 x2 x3 x4 (up to x9 (lower case))):", bg="white").grid(row=5, column=0, sticky=W)
L5Entry = Entry (window, width=20, bg="white")
L5Entry.grid(row=5, column=2, sticky=W)

L6 = Label(window, text="", bg="white").grid(row=6, column=0, sticky=W)

L7 = Label(window, text="constraints:\n(ex:1*x1+3*x2<=10_-1*x2+2*x3<=5)", bg="white").grid(row=7, column=0, sticky=W)
L7Entry = Entry (window, width=20, bg="white")
L7Entry.grid(row=7, column=2, sticky=W)

Button(window, text= "Execute", width=6, command=click).grid(row=8, column = 1)


window.mainloop()
