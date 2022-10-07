import tkinter
from tkinter import ttk

window= tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

username_label = ttk.Label(window,text="Selecciona tu helado fav")
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=50, pady=10)


lista=['chocolate','fresa','vainilla']
lista_items=tkinter.StringVar(value=lista)

listbox=tkinter.Listbox(window, height=100, listvariable=lista_items)
listbox.grid(column=0,row=1, sticky=tkinter.W, padx=50)

window.mainloop()