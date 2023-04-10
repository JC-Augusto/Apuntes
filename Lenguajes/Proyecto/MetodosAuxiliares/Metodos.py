from tkinter import*
from tkinter import filedialog

def cargarArchivo() -> str:
    """Devuelve la ruta del archivo"""
    archivo = filedialog.askopenfilename(filetypes=(("Archivos pxla","*.pxla"),("Archivos de texto","*.txt")), title="Seleccione el archivo")
    return archivo

def centrarVentana(ancho, alto,raizX,raizY):
    x_ventana = raizX // 2 - ancho // 2
    y_ventana = raizY // 2 - alto // 2
    posicion = str(ancho) + "x" + str(alto) + "+" + str(x_ventana) + "+" + str(y_ventana)
    return posicion