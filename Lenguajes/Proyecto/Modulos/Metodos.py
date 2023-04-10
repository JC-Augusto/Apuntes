from tkinter import*
from tkinter import filedialog

def cargarArchivo() -> str:
    """Devuelve la ruta del archivo"""
    archivo = filedialog.askopenfilename(filetypes=(("Archivos pxla","*.pxla"),("Archivos de texto","*.txt")), title="Seleccione el archivo")
    return archivo

def leerArchivo(ruta):
    archivo = open(ruta, 'r')
    contenido = archivo.read()
    archivo.close()
    return contenido