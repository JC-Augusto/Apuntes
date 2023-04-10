import sys
sys.path.append(".")
from tkinter import *
from MetodosAuxiliares import *

def crearVentana():
    raiz = Tk()
    raiz.title("[LFP]Proyecto 1")
    raiz.iconbitmap("Imagenes/jcaLogo.ico")
    raiz.config(bg ="black")
    raiz.geometry(centrarVentana(800,500,raiz.winfo_screenwidth(),raiz.winfo_screenheight()))
    miFrame = Frame(raiz, width="1000", height="1000").pack(fill="both", expand="True")


def crearBoton():
    boton = Button()
    pass