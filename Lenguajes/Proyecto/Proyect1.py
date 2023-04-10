from tkinter import *
from MetodosAuxiliares.Metodos import *

raiz = Tk()
raiz.title("[LFP]Proyecto 1")
raiz.iconbitmap("Imagenes/jcaLogo.ico")
raiz.config(bg ="black")
raiz.geometry(centrarVentana(800,500,raiz.winfo_screenwidth(),raiz.winfo_screenheight()))

miFrame = Frame(raiz, width="600", height="400")
miFrame.config(bg = "green")
miFrame.pack(fill="both", expand="True")
ruta = cargarArchivo()
botonCargar = Button(miFrame, text="Exportar", command=lambda:cargarArchivo())

botonCargar.grid(row=0, column=0)

def rutaAr():
    print(ruta)
    pass

botonAnalizar = Button(miFrame, text="Analizar",command=lambda:rutaAr())
botonAnalizar.grid(row=0, column=1)

botonReportes = Button(miFrame, text="Reportes", )
botonReportes.grid(row=0, column=2)

botonSalir = Button(miFrame, text="Salir", command=lambda:raiz.destroy())
botonSalir.grid(row=0, column=3)



raiz.mainloop()