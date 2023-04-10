
from tkinter import Tk,Text,Button,END,re
from Modulos.Analizador import Analizador
from Modulos.FuncionesAuxiliares import *
import webbrowser

scanner = Analizador()

class Interfaz:
    def __init__(self, ventana):
        #Inicializar la ventana con un título
        self.ventana=ventana
        self.ventana.title("Proyecto 2")

        self.pantalla=Text(self.ventana, width=55, height=25, background="gray16", foreground="white", font=("Helvetica",10))
        self.pantalla2=Text(self.ventana, width=70, height=25, background="gray16", foreground="white", font=("Helvetica",10))
        #Ubicar la pantalla en la ventana
        self.pantalla.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
        self.pantalla2.grid(row=1, column=4, columnspan=4, padx=5, pady=5)

        boton1 = Button(self.ventana, text = "Abrir", width= 10, height = 1,command=lambda:self.mostrarEnPantalla(leerArchivo(rutaArchivo())))
        boton2 = Button(self.ventana, text = "Analizar", width= 10, height = 1,command=lambda:self.mostrarEnPantalla2())
        boton3 = Button(self.ventana, text = "Errores Sintacticos", width= 15, height = 1,command=lambda:scanner.generarTablaErroresSintacticos())
        boton4 = Button(self.ventana, text = "Errores Lexicos", width= 15, height = 1, command=lambda:scanner.generarTablaErrores())
        boton5 = Button(self.ventana, text = "TOKENS", width= 15, height = 1, command=lambda:scanner.generarTablaTokens())

        #Ubicar los botones con el gestor grid
        boton1.grid(row=0,column=0)
        boton2.grid(row=0,column=1)
        boton3.grid(row=0,column=2)
        boton4.grid(row=0,column=3)
        boton5.grid(row=0,column=4)

    def obtener(self):
        texto = self.pantalla.get("1.0",'end-1c')
        return texto
    
    def analizarPantalla(self):
        return scanner.analizar(self.obtener())
        

    def mostrarEnPantalla2(self):
        self.pantalla2.configure(state="normal")
        self.pantalla2.delete("1.0", END)
        self.pantalla2.insert(END, self.analizarPantalla())
        self.pantalla2.configure(state="disabled")
        return

    def mostrarEnPantalla(self, valor):
        self.pantalla.insert(END, valor)
        
        return
    def limpiarPantalla(self):
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0", END)
        self.pantalla.configure(state="disabled")
        return

ventana_principal=Tk()
proy=Interfaz(ventana_principal)
ventana_principal.mainloop()