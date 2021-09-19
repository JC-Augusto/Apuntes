from tkinter import *

#Creando la ventana principal 
raiz = Tk()
raiz.title("Titulo de la ventana")
raiz.resizable(True,True) #Acepta valores voleanos 0 o 1 para (with,heigh),(ancho, alto) impide el redimencionamiento
raiz.iconbitmap("Ventanas/JCA.ico")
#raiz.geometry("400x500")
raiz.config(bg="white")
#para que se ejecute como aplicacion cambiar extención a "*.pyw"

#Creando el frame (que va dentro de la ventana)
miFrame = Frame()
miFrame.pack(fill="both", expand="True") #enpaquetando el frame con la raiz para que sean uno solo
miFrame.config(bg="black")
miFrame.config(width="400", height="500")
raiz.mainloop() #para que la ventana se acualice y este en observacion de acciones
