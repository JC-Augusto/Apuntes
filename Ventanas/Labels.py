from tkinter import *

root = Tk()
miFrame = Frame(root, width=600, height= 400)
miFrame.config(bg="black")
miFrame.pack()

miLabel = Label(miFrame, text="Primer texto", bg="black",fg="white",font=("arial", 20)).place(x=20,y=20)
miImagen = PhotoImage(file = "Ventanas/J logo.png")
#miLabel2 = Label(miFrame, image= miImagen, bg= "black").place(x=40,y= 50)
def codigoBotonEjemplo():
    print("hola")
botonEjemplo = Button(miFrame, text= "Ejemplo", command=codigoBotonEjemplo).pack()
botonEjemplo.grid(row=4,column=6,sticky="e")




root.mainloop()