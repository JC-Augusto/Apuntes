from tkinter import*
from tkinter import filedialog

def rutaArchivo() -> str:
    """Devuelve la ruta del archivo"""
    archivo = filedialog.askopenfilename(filetypes=(("Archivos lfp","*.lfp"),("Archivos de texto","*.txt")), title="Seleccione el archivo")
    return archivo