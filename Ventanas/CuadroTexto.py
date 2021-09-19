from tkinter import *

raiz = Tk()
miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

def accionBotonEjemplo():
    print("hola")

def quit(self): 
    self.root.destroy()
cuadroTexto = Entry(miFrame)
cuadroTexto.grid(row=0, column=1, padx=10)
nombreLabel=Label(miFrame, text="Nombre:")  
nombreLabel.grid(row=0,column=0, sticky="e", padx=10)


botonEjemplo = Button(miFrame, text="Analizar", command=accionBotonEjemplo)
botonEjemplo.grid(row=0,column=2, sticky="e",)

botonEjemplo = Button(miFrame, text="Reportes", command=accionBotonEjemplo)
botonEjemplo.grid(row=0,column=2, sticky="e",)

botonEjemplo = Button(miFrame, text="Salir", command=quit)
botonEjemplo.grid(row=0,column=2, sticky="e",)

raiz.mainloop()