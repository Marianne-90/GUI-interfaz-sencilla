import tkinter

window = tkinter.Tk()
label_saludo=tkinter.Label(window, text="hola", bg="yellow", fg="blue")
label_saludo.pack(ipadx=50,ipady=50,fill="both",side="right")
label_adios=tkinter.Label(window, text="adios", bg="red", fg="blue")
label_adios.pack(fill="both", side="left")

window.mainloop()