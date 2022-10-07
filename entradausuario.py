import tkinter
from tkinter import ttk

window= tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

#usuario
#etiqueta usuario
username_label = ttk.Label(window,text="Username:")
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

username_entry = ttk.Entry(window)
username_entry.grid(column=1,row=0, sticky=tkinter.E,  padx=5, pady=5)

#etiqueta pasword          
password_label = ttk.Label(window,text="Pasword:")
password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

password_entry = ttk.Entry(window, show='*')
password_entry.grid(column=1,row=1, sticky=tkinter.E,  padx=5, pady=5) 

##Boton
login_boton=ttk.Button(window, text="Login")
login_boton.grid(column=1, row=3, sticky=tkinter.E, padx=5, pady=5)

window.mainloop()