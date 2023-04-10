from tkinter.constants import CASCADE
from Modulos.Token import Token
from Modulos.Errores import Errores
from Modulos.DatosImagen import datosImagen
from Modulos.ColoresImagen import coloresImagen
from prettytable import PrettyTable
from Modulos.FuncionesAuxiliares import *
class Analizador:

    def __init__(self):
        self.palabrasReservadas = ["TITULO","ANCHO","ALTO","FILAS","COLUMNAS","CELDAS","FILTROS","MIRRORX","MIRRORY","DOUBLEMIRROR","FALSE","TRUE","@@@@"]
        
        #lista para el automata
        self.listaTokens = []
        self.listaErrores = []

        #Lista de los datos de imagenes
        self.listaDatosImagenes = []
        self.listaColores = []
        self.listaFiltros = []

        self.px = None
        self.py = None
        self.boo = None
        self.col = None

        #datos automata
        self.estado = 0
        self.indexCadena = 0
        self.linea = 1
        self.columna = 0
        self.buffer = ''
        self.contadorAuxiliar = 0

        #Datos para el programa
        self.titulo = ""
        self.ancho = ""
        self.alto = ""
        self.filas = ""
        self.columnas = ""
        self.varAuxiliar = ""


        self.aceptacionDeNuevaImagen = False
        self.listadeListaDeColores = []
        self.listadeListaDeDatos = []
        self.listadeListaFiltros = []
        

    #Datos para el Automata
    def analizar(self, cadena):
        cadena +="\n@@@@█"
        self.estado = 0
        self.indexCadena = 0

        while self.indexCadena < len(cadena): 
            if self.estado == 0:
                self.estado0(cadena[self.indexCadena])
            elif self.estado == 1:
                self.estado1(cadena[self.indexCadena])
            elif self.estado == 2:
                self.estado2(cadena[self.indexCadena])
            elif self.estado == 3:
                self.estado3(cadena[self.indexCadena])
            elif self.estado == 4:
                self.estado4(cadena[self.indexCadena])
            elif self.estado == 5:
                self.estado5(cadena[self.indexCadena])
            elif self.estado == 6:
                self.estado6(cadena[self.indexCadena])
            elif self.estado == 7:
                self.estado7(cadena[self.indexCadena])
            elif self.estado == 8:
                self.estado8(cadena[self.indexCadena])
            elif self.estado == 9:
                self.estado9(cadena[self.indexCadena])
            elif self.estado == 10:
                self.estado10(cadena[self.indexCadena])
            elif self.estado == 11:
                self.estado11(cadena[self.indexCadena])
            elif self.estado == 12:
                self.estado12(cadena[self.indexCadena])
            elif self.estado == 13:
                self.estado13(cadena[self.indexCadena])
            elif self.estado == 14:
                self.estado14(cadena[self.indexCadena])
            elif self.estado == 15:
                self.estado15(cadena[self.indexCadena])
            elif self.estado == 16:
                self.estado16(cadena[self.indexCadena])
            elif self.estado == 17:
                self.estado17(cadena[self.indexCadena])
            elif self.estado == 18:
                self.estado18(cadena[self.indexCadena])
            elif self.estado == 19:
                self.estado19(cadena[self.indexCadena])
            elif self.estado == 20:
                self.estado20(cadena[self.indexCadena])
            self.indexCadena += 1
    def agregarError(self, caracter, linea, columna): 
        self.listaErrores.append(Errores("Caracter "+str(caracter)+ " No reconocido en el lenguaje",linea, columna))
    def agregarToken(self, lexema, token, linea, columna):
        self.listaTokens.append(Token(lexema, token, linea, columna))

    #Datos para el programa
    def agregarDatosImagen(self, titulo, ancho, alto, fila, columna):
        self.listaDatosImagenes.append(datosImagen(titulo, ancho, alto, fila, columna))

    def agregarColoresImagen(self, x, y, booleano, color): 
        self.listaColores.append(coloresImagen(x,y,booleano,color))

    def movimientoEstado(self, movColumna, movLinea, movEstado, agregarBuffer):
        if movColumna == "reset":
            self.columna = 1
        else: 
            self.columna += movColumna
        self.linea += movLinea
        self.estado = movEstado
        if agregarBuffer == "":
            self.buffer = ""
        else:
            self.buffer += agregarBuffer
    
    def descripicionMovimientoEstado(self, caracter):
        print(f"voy al estado {self.estado} y llevo -{caracter}- con cadena -{self.buffer}- en columna: {self.columna} y linea: {self.linea}")
    
    def agregarListaDeColores(self):
        self.listadeListaDeColores.append(self.listaColores)
    
    def agregarListaDeDatos(self): 
        self.listadeListaDeDatos.append(self.listaDatosImagenes)

    def estado0(self, caracter):
        if self.buffer in self.palabrasReservadas:
            self.agregarToken(self.buffer, "SeparadorImagen", self.linea, self.columna-1)
            if self.aceptacionDeNuevaImagen == True:
                self.agregarListaDeColores()
                self.agregarListaDeDatos()
                self.listadeListaFiltros.append(self.listaFiltros)
                self.listaFiltros = []
                self.listaDatosImagenes = []
                self.listaColores = []
                self.aceptacionDeNuevaImagen = False               
            self.movimientoEstado(0,0,1,"")
            self.indexCadena -= 1
        else:
            if caracter == "@":
                self.movimientoEstado(1,0,0,caracter)
            elif caracter.isalpha():
                self.movimientoEstado(1,0,1,caracter)  
            elif caracter == "\n":
                self.movimientoEstado("reset",1,0,"")
            elif caracter == " ":
                self.movimientoEstado(1,0,0,"")
            elif caracter == "\t":
                self.movimientoEstado(4,0,0,"")
            elif caracter == " ":
                self.movimientoEstado(1,0,0,"")
            else:
                self.agregarError(caracter, self.linea, self.columna)
                self.movimientoEstado(1,0,0,"")

    def estado1(self, caracter):
        if self.buffer in self.palabrasReservadas:
            self.varAuxiliar = self.buffer
            self.agregarToken(self.buffer, "palabraReservada",self.linea,self.columna-1)
            self.movimientoEstado(0,0,1,"")
            self.indexCadena -=1
        else: 
            if caracter == "=":
                self.agregarToken(caracter, "signoIgual", self.linea, self.columna)
                self.movimientoEstado(1,0,2,"")
            elif caracter.isalpha():
                self.movimientoEstado(1,0,1,caracter)
            elif caracter == " ":
                self.movimientoEstado(1,0,1,"")
            elif caracter == "\n":
                self.movimientoEstado("reset",1,1,"")
            elif caracter == "\t":
                self.movimientoEstado(4,0,1,"")
            elif caracter == "█":
                self.movimientoEstado(1,0,0,"")
            else:
                self.agregarError(caracter,self.linea, self.columna)
                self.movimientoEstado(1,0,1,"")

    def estado2(self, caracter):
        if caracter == "\"":
            self.movimientoEstado(1,0,3,"")
            self.agregarToken(caracter, "Comillas", self.linea, self.columna)
        elif caracter.isdigit():
            self.movimientoEstado(1,0,4,caracter)
        elif caracter == " ":
            self.movimientoEstado(1,0,2,"")
        elif caracter.isalpha():
            self.movimientoEstado(1,0,6,caracter)
        elif caracter == "{":
            self.agregarToken(caracter,"CorcheteAbierto", self.linea, self.columna)
            self.movimientoEstado(1,0,5,"")
        elif caracter == "\t":
            self.movimientoEstado(4,0,2,"")
        elif caracter == "\n":
            self.movimientoEstado("reset", 1,2,"")
        else:
            self.agregarError(caracter,self.linea,self.columna)
            self.movimientoEstado(1,0,2,"")

    def estado3(self, caracter):
        if caracter.isalpha():
            self.movimientoEstado(1,0,7,caracter)
        elif caracter == " ":
            self.movimientoEstado(1,0,3,"")
        elif caracter == "\n":
            self.movimientoEstado("reset",1,3,"")
        elif caracter == "\t":
            self.movimientoEstado(4,0,3,"")
        else:
            self.agregarError(caracter,self.linea,self.columna-1)
            self.movimientoEstado(1,0,3,"")

    def estado4(self, caracter):
        if caracter.isdigit():
            self.movimientoEstado(1,0,4,caracter)
        elif caracter == " ":
            self.movimientoEstado(1,0,4,"")
        elif caracter == "\n":
            self.movimientoEstado("reset",1,4,"")
        elif caracter == "\t":
            self.movimientoEstado(4,0,4,"")
        elif caracter == ";":
            if self.varAuxiliar == "ANCHO":
                self.ancho = self.buffer
            elif self.varAuxiliar == "ALTO":
                self.alto = self.buffer
            elif self.varAuxiliar == "FILAS":
                self.filas = self.buffer
            elif self.varAuxiliar == "COLUMNAS":
                self.columnas = self.buffer
            self.agregarToken(self.buffer,"Digito",self.linea,self.columna-1)
            self.agregarToken(caracter,"puntoYComa", self.linea,self.columna)
            self.movimientoEstado(1,0,0,"")
        else:
            self.agregarError(caracter,self.linea,self.columna)
            self.movimientoEstado(1,0,4,"")

    def estado5(self, caracter):
        if caracter == "[":
            self.agregarToken(caracter,"CorcheteAbierto", self.linea, self.columna)
            self.movimientoEstado(1,0,8,"")
        elif caracter == " ":
            self.movimientoEstado(1,0,5,"")
        elif caracter == "\n":
            self.movimientoEstado("reset",1,5,"")
        elif caracter == "\t":
            self.movimientoEstado(4,0,5,"")
        else:
            self.agregarError(caracter,self.linea,self.columna)
            self.movimientoEstado(1,0,5,"")

    def estado6(self, caracter):
        if caracter.isalpha():
            self.movimientoEstado(1,0,9,caracter)
        elif caracter == ",":
            self.movimientoEstado(1,0,10,"")
        elif caracter == ";":
            self.movimientoEstado(1,0,0,"")
        elif caracter == " ":
            self.movimientoEstado(1,0,6,"")
        elif caracter == "\n":
            self.movimientoEstado("reset",1,6,"")
        elif caracter == "\t":
            self.movimientoEstado(4,0,6,"")
        else:
            self.agregarError(caracter,self.linea,self.columna)
            self.movimientoEstado(1,0,6,"")

    def estado7(self, caracter):
        if caracter.isalpha() or caracter.isdigit() or caracter == " ":
            self.movimientoEstado(1,0,7,caracter)
        elif  caracter == "\"":
            self.titulo = self.buffer
            self.agregarToken(self.buffer, "NombreImagen", self.linea, self.columna-1)
            self.movimientoEstado(1,0,11,"")
        elif caracter == "\n":
            self.movimientoEstado("reset",1,7,"")
        elif caracter == "\t":
            self.movimientoEstado(4,0,7,"")
        else:  
            self.agregarError(caracter,self.linea,self.columna)
            self.movimientoEstado(1,0,7,"")

    def estado8(self, caracter):
        if caracter.isdigit():
            self.movimientoEstado(1,0,12,caracter)
        elif caracter == " ":
            self.movimientoEstado(1,0,8,"")
        elif caracter == "\n":
            self.movimientoEstado("reset",1,8,"")
        elif caracter == "\t":
            self.movimientoEstado(4,0,8,"")
        else:
            self.agregarError(caracter,self.linea,self.columna)
            self.movimientoEstado(1,0,8,"")

    def estado9(self, caracter):
        if self.buffer in self.palabrasReservadas:
            self.listaFiltros.append(self.buffer)
            self.agregarToken(self.buffer, "palabraReservada",self.linea,self.columna-1)
            self.movimientoEstado(0,0,9,"")
            self.indexCadena -=1
        else: 
            if caracter.isalpha():
                self.movimientoEstado(1,0,9,caracter)
            elif caracter == ",":
                self.agregarToken(caracter,"coma",self.linea,self.columna)
                self.movimientoEstado(1,0,10,"")
            elif caracter == ";":
                if self.titulo != "" and self.ancho != "" and self.alto != "" and self.filas != "" and self.columnas != "":
                    self.aceptacionDeNuevaImagen = True
                    self.agregarDatosImagen(self.titulo,self.ancho, self.alto, self.filas, self.columnas)
                    self.titulo, self.ancho, self.alto, self.filas, self.columnas = "", "", "", "", ""
                    self.movimientoEstado(1,0,0,"")
                else:
                    print("No se cargaron los datos suficientes para la imagen")
                self.agregarToken(caracter,"puntoYComa",self.linea,self.columna)
                self.movimientoEstado(1,0,0,"")
            elif caracter == " ":
                self.movimientoEstado(1,0,9,"")
            elif caracter == "\n":
                self.movimientoEstado("reset",1,9,"")
            elif caracter == "\t":
                self.movimientoEstado(4,0,9,"")
            else:
                self.agregarError(caracter,self.linea,self.columna)
                self.movimientoEstado(1,0,9,"")
    def estado10(self, caracter):
        if caracter.isalpha():
            self.movimientoEstado(1,0,6,caracter)
        elif caracter == " ":
            self.movimientoEstado(1,0,10,"")
        elif caracter == "\n":
            self.movimientoEstado("reset",1,10,"")
        elif caracter == "\t":
            self.movimientoEstado(4,0,10,"")
        else:
            self.agregarError(caracter,self.linea,self.columna)
            self.movimientoEstado(1,0,10,"")

    def estado11(self, caracter):
        if caracter == ";":
            self.agregarToken(caracter, "puntoYComa", self.linea, self.columna)
            self.movimientoEstado(1,0,0,"")
        elif caracter == " ":
            self.movimientoEstado(1,0,11,"")
        elif caracter == "\n":
            self.movimientoEstado("reset",1,11,"")
        elif caracter == "\t":
            self.movimientoEstado(4,0,11,"")
        else:
            self.agregarError(caracter,self.linea,self.columna)
            self.movimientoEstado(1,0,11,"")

    def estado12(self, caracter):
        if caracter.isdigit():
            self.movimientoEstado(1,0,12,caracter)
        elif caracter == ",":
            self.px = int(self.buffer)
            self.agregarToken(self.buffer, "digito", self.linea, self.columna-1)
            self.agregarToken(caracter, "coma", self.linea, self.columna)
            self.movimientoEstado(1,0,13,"")
        elif caracter == " ":
            self.movimientoEstado(1,0,12,"")
        elif caracter == "\n":
            self.movimientoEstado("reset",1,12,"")
        elif caracter == "\t":
            self.movimientoEstado(4,0,12,"")
        else:
            self.agregarError(caracter,self.linea,self.columna)
            self.movimientoEstado(1,0,12,"")

    def estado13(self, caracter):
        if caracter.isdigit():
            self.movimientoEstado(1,0,14,caracter)
        elif caracter == " ":
            self.movimientoEstado(1,0,13,"")
        elif caracter == "\n":
            self.movimientoEstado("reset",1,13,"")
        elif caracter == "\t":
            self.movimientoEstado(4,0,13,"")
        else:
            self.agregarError(caracter,self.linea,self.columna)
            self.movimientoEstado(1,0,13,"")

    def estado14(self, caracter):
        if caracter.isdigit():
            self.movimientoEstado(1,0,14,caracter)
        elif caracter == ",":
            self.py = int(self.buffer)
            self.agregarToken(self.buffer, "digito", self.linea, self.columna-1)
            self.agregarToken(caracter, "coma", self.linea, self.columna)
            self.movimientoEstado(1,0,15,"")
        elif caracter == " ":
            self.movimientoEstado(1,0,14,"")
        elif caracter == "\n":
            self.movimientoEstado("reset",1,14,"")
        elif caracter == "\t":
            self.movimientoEstado(4,0,14,"")
        else: 
            self.agregarError(caracter,self.linea,self.columna)
            self.movimientoEstado(1,0,14,"")

    def estado15(self, caracter):
        if self.buffer in self.palabrasReservadas:
            self.boo = self.buffer
            self.agregarToken(self.buffer, "Booleano", self.linea, self.columna-1)
            self.movimientoEstado(0,0,16,"")
            self.indexCadena -=1
        else:
            if caracter.isalpha():
                self.movimientoEstado(1,0,15,caracter)
            elif caracter == " ":
                self.movimientoEstado(1,0,15,"")
            elif caracter == "\n":
                self.movimientoEstado("reset",1,15,"")
            elif caracter == "\t":
                self.movimientoEstado(4,0,15,"")
            else:
                self.agregarError(caracter,self.linea,self.columna)
                self.movimientoEstado(1,0,15,"")

    def estado16(self, caracter):
        if caracter == ",":
            self.agregarToken(caracter, "coma", self.linea, self.columna)
            self.movimientoEstado(1,0,17,"")
            self.contadorAuxiliar = 0
        elif caracter == " ":
            self.movimientoEstado(1,0,16,"")
        elif caracter == "\n":
            self.movimientoEstado("reset",1,16,"")
        elif caracter == "\t":
            self.movimientoEstado(4,0,16,"")
        else:
            self.agregarError(caracter,self.linea,self.columna)
            self.movimientoEstado(1,0,16,"")

    def estado17(self, caracter):
        if self.contadorAuxiliar < 7:
            if caracter == "#":
                self.movimientoEstado(1,0,17,caracter)
                self.contadorAuxiliar +=1
                
            elif caracter.isdigit() or caracter.isalpha():
                self.movimientoEstado(1,0,17,caracter)
                self.contadorAuxiliar +=1
            else:
                self.agregarError(caracter,self.linea,self.columna)
                self.movimientoEstado(1,0,17,"")
        else:
            self.col = self.buffer
            self.agregarColoresImagen(self.px,self.py,self.boo,self.col)
            self.py, self.px, self.boo, self.col = None,None,None,None
            self.agregarToken(self.buffer, "Color HTML", self.linea, self.columna-1)
            self.movimientoEstado(0,0,18,"")
            self.indexCadena -=1

    def estado18(self, caracter):
        if caracter == "]":
            self.agregarToken(caracter, "corcheteCerrado", self.linea, self.columna)
            self.movimientoEstado(1,0,19,"")
        elif caracter == " ":
            self.movimientoEstado(1,0,18,"")
        elif caracter == "\n":
            self.movimientoEstado("reset",1,18,"")
        elif caracter == "\t":
            self.movimientoEstado(4,0,18,"")
        else: 
            self.agregarError(caracter,self.linea,self.columna)
            self.movimientoEstado(1,0,18,"")

    def estado19(self, caracter):
        if caracter == ",":
            self.agregarToken(caracter, "coma", self.linea, self.columna)
            self.movimientoEstado(1,0,5,"")
        elif caracter == "}":
            self.agregarToken(caracter, "llaveCerrada", self.linea, self.columna)
            self.movimientoEstado(1,0,20,"")
        elif caracter == " ":
            self.movimientoEstado(1,0,19,"")
        elif caracter == "\n":
            self.movimientoEstado("reset",1,19,"")
        elif caracter == "\t":
            self.movimientoEstado(4,0,19,"")
        else:
            self.agregarError(caracter,self.linea,self.columna)
            self.movimientoEstado(1,0,19,"")

    def estado20(self, caracter):
        self.descripicionMovimientoEstado
        if caracter == ";":
            self.agregarToken(caracter, "puntoYComa", self.linea, self.columna)
            self.movimientoEstado(1,0,0,"")
        elif caracter == " ":
            self.movimientoEstado(1,0,20,"")
        elif caracter == "\n":
            self.movimientoEstado("reset",1,20,"")
        elif caracter == "\t":
            self.movimientoEstado(4,0,20,"")
        else:
            self.agregarError(caracter,self.linea,self.columna)
            self.movimientoEstado(1,0,20,"")
    
    def imprimirErrores(self):
        x = PrettyTable()
        x.field_names = ["Descripcion", "Fila", "Columna"]
        if len(self.listaErrores)==0:
            print('No hay errores')
        else:
            for i in self.listaErrores:
                x.add_row(i.enviarData())
            print(x)

    def imprimirTokens(self):
        x = PrettyTable()
        x.field_names = ["Lexema", "Token", "Fila", "Columna"]
        for i in self.listaTokens:
            x.add_row(i.enviarData())
        print(x)
    
    def imprimirListaColores(self):
        x = PrettyTable()
        x.field_names = ["px", "py", "booleano", "Color"]
        for i in self.listaColores:
            x.add_row(i.enviarData())
        print(x)


    def imprimirDatosImagen(self):
        x = PrettyTable()
        x.field_names = ["Titulo", "ancho", "alto","filas", "Columnas"]
        for i in self.listaDatosImagenes:
            x.add_row(i.enviarData())
        print(x)
    
    def generarTablaErrores(self):
        head = EncabezadoErrores()
        bottom = finalhtml()
        body = ""
        for datos in self.listaErrores:
            body += f"""
                    <tr>
                        <td>{datos.enviarData()[0]}</td>
                        <td>{datos.enviarData()[1]}</td>                                            
                        <td>{datos.enviarData()[2]}</td>                        
                    </tr>"""   
        html = open("Proyecto1/templates/ListaErroes.html",'w+')
        html.write(head+body+bottom)

    def generarTablaTokens(self):
        head = EncabezadoTokens()
        bottom = finalhtml()
        body = ""
        for datos in self.listaTokens:
            body += f"""
                    <tr>
                        <td>{datos.enviarData()[0]}</td>
                        <td>{datos.enviarData()[1]}</td>                                            
                        <td>{datos.enviarData()[2]}</td>  
                        <td>{datos.enviarData()[3]}</td>                      
                    </tr>"""   
        html = open("Proyecto1/templates/ListaTokens.html",'w+')
        html.write(head+body+bottom)


    def generarImagenOriginal(self):
        nombreImagen = self.listaDatosImagenes[0].enviarData()[0]
        anchoColuma = self.listaDatosImagenes[0].enviarData()[1]
        altoColuma = self.listaDatosImagenes[0].enviarData()[2]
        filasImagen = self.listaDatosImagenes[0].enviarData()[3]
        columnasImagen = self.listaDatosImagenes[0].enviarData()[4]

        head = EncabezadoImagen()
        bottom = finalhtml()
        body = ""

        for i in range(0,int(filasImagen)):
            body += f"""\t\t\t\t<tr HEIGHT="{int(altoColuma)/int(filasImagen)}">\n"""
            for j in range(0,int(columnasImagen)):
                continuar = False
                for indice in range(0,len(self.listaColores)):
                    if j == self.getColor(indice,0) and i == self.getColor(indice,1) and self.getColor(indice,2) == "TRUE":
                        body += f"""\t\t\t\t\t<td WIDTH="{int(anchoColuma)/int(columnasImagen)}" style="background-color: {self.getColor(indice,3)}"></td>\n"""
                        continuar = True
                        break
                if continuar == False:
                    body += f"""\t\t\t\t\t<td WIDTH="{int(anchoColuma)/int(columnasImagen)}" style="background-color: #FFFFFF"></td>\n"""
                continuar = False
            body += "\t\t\t\t</tr>\n"

        html = open(f"Proyecto1/templates/{nombreImagen}.html",'w+')
        html.write(head+body+bottom)


    def generarImagenMirrorX(self):
        nombreImagen = self.listaDatosImagenes[0].enviarData()[0]
        anchoColuma = self.listaDatosImagenes[0].enviarData()[1]
        altoColuma = self.listaDatosImagenes[0].enviarData()[2]
        filasImagen = self.listaDatosImagenes[0].enviarData()[3]
        columnasImagen = self.listaDatosImagenes[0].enviarData()[4]

        head = EncabezadoImagen()
        bottom = finalhtml()
        body = ""

        for i in range(0,int(filasImagen)):
            body += f"""\t\t\t\t<tr HEIGHT="{int(altoColuma)/int(filasImagen)}">\n"""
            for j in range(int(columnasImagen)-1,-1,-1):
                continuar = False
                for indice in range(0,len(self.listaColores)):
                    if j == self.getColor(indice,0) and i == self.getColor(indice,1) and self.getColor(indice,2) == "TRUE":
                        body += f"""\t\t\t\t\t<td WIDTH="{int(anchoColuma)/int(columnasImagen)}" style="background-color: {self.getColor(indice,3)}"></td>\n"""
                        continuar = True
                        break
                if continuar == False:
                    body += f"""\t\t\t\t\t<td WIDTH="{int(anchoColuma)/int(columnasImagen)}" style="background-color: #FFFFFF"></td>\n"""
                continuar = False
            body += "\t\t\t\t</tr>\n"

        html = open(f"Proyecto1/templates/{nombreImagen}_MirrorX.html",'w+')
        html.write(head+body+bottom)

    def generarImagenDoubleMirror(self):
        nombreImagen = self.listaDatosImagenes[0].enviarData()[0]
        anchoColuma = self.listaDatosImagenes[0].enviarData()[1]
        altoColuma = self.listaDatosImagenes[0].enviarData()[2]
        filasImagen = self.listaDatosImagenes[0].enviarData()[3]
        columnasImagen = self.listaDatosImagenes[0].enviarData()[4]

        head = EncabezadoImagen()
        bottom = finalhtml()
        body = ""

        for i in range(int(filasImagen)-1,-1,-1):
            body += f"""\t\t\t\t<tr HEIGHT="{int(altoColuma)/int(filasImagen)}">\n"""
            for j in range(int(columnasImagen)-1,-1,-1):
                continuar = False
                for indice in range(0,len(self.listaColores)):
                    if j == self.getColor(indice,0) and i == self.getColor(indice,1) and self.getColor(indice,2) == "TRUE":
                        body += f"""\t\t\t\t\t<td WIDTH="{int(anchoColuma)/int(columnasImagen)}" style="background-color: {self.getColor(indice,3)}"></td>\n"""
                        continuar = True
                        break
                if continuar == False:
                    body += f"""\t\t\t\t\t<td WIDTH="{int(anchoColuma)/int(columnasImagen)}" style="background-color: #FFFFFF"></td>\n"""
                continuar = False

            body += "\t\t\t\t</tr>\n"

        html = open(f"Proyecto1/templates/{nombreImagen}_DoubleMirror.html",'w+')
        html.write(head+body+bottom)

    def generarImagenMirrorY(self):
        nombreImagen = self.listaDatosImagenes[0].enviarData()[0]
        anchoColuma = self.listaDatosImagenes[0].enviarData()[1]
        altoColuma = self.listaDatosImagenes[0].enviarData()[2]
        filasImagen = self.listaDatosImagenes[0].enviarData()[3]
        columnasImagen = self.listaDatosImagenes[0].enviarData()[4]

        head = EncabezadoImagen()
        bottom = finalhtml()
        body = ""

        for i in range(int(filasImagen)-1,-1,-1):
            body += f"""\t\t\t\t<tr HEIGHT="{int(altoColuma)/int(filasImagen)}">\n"""
            for j in range(0,int(columnasImagen)):
                continuar = False
                for indice in range(0,len(self.listaColores)):
                    if j == self.getColor(indice,0) and i == self.getColor(indice,1) and self.getColor(indice,2) == "TRUE":
                        body += f"""\t\t\t\t\t<td WIDTH="{int(anchoColuma)/int(columnasImagen)}" style="background-color: {self.getColor(indice,3)}"></td>\n"""
                        continuar = True
                        break
                if continuar == False:
                    body += f"""\t\t\t\t\t<td WIDTH="{int(anchoColuma)/int(columnasImagen)}" style="background-color: #FFFFFF"></td>\n"""
                continuar = False

            body += "\t\t\t\t</tr>\n"

        html = open(f"Proyecto1/templates/{nombreImagen}_MirrorY.html",'w+')
        html.write(head+body+bottom)


    def getColor(self,indice,valor):
        return self.listaColores[indice].enviarData()[valor]

    def getName(self):
        return self.listadeListaDeDatos[0][0].enviarData()[0]
        #1 - nombre de cual imagen 
        #2 - va 0 f
        #3 - 0 por que es el dato 0 del vector (osea el nombre)
    
    def getNewColor(self,archivo,indice,valor):
        return self.listadeListaDeColores[archivo][indice].enviarData()[valor]
        #1 = de que imagen
        #2 = de que vector de esa imagen 
        #3 = de que dato de ese vector

    def getFiltros(self): 
        return self.listadeListaFiltros[0][0]
        #1 = de que imagen
        #2 = cual de esa imagen 

    def getTamañoListaDeListas(self):
        return len(self.listadeListaDeColores)

    def generarImagenOriginalVarios(self,archivo):
        nombreImagen = self.listadeListaDeDatos[archivo][0].enviarData()[0]
        anchoColuma = self.listadeListaDeDatos[archivo][0].enviarData()[1]
        altoColuma = self.listadeListaDeDatos[archivo][0].enviarData()[2]
        filasImagen = self.listadeListaDeDatos[archivo][0].enviarData()[3]
        columnasImagen = self.listadeListaDeDatos[archivo][0].enviarData()[4]

        head = EncabezadoImagen()
        bottom = finalhtml()
        body = ""

        for i in range(0,int(filasImagen)):
            body += f"""\t\t\t\t<tr HEIGHT="{int(altoColuma)/int(filasImagen)}">\n"""
            for j in range(0,int(columnasImagen)):
                continuar = False
                for indice in range(0,len(self.listadeListaDeColores[archivo])):
                    if j == self.getNewColor(archivo,indice,0) and i == self.getNewColor(archivo,indice,1) and self.getNewColor(archivo,indice,2) == "TRUE":
                        body += f"""\t\t\t\t\t<td WIDTH="{int(anchoColuma)/int(columnasImagen)}" style="background-color: {self.getNewColor(archivo,indice,3)}"></td>\n"""
                        continuar = True
                        break
                if continuar == False:
                    body += f"""\t\t\t\t\t<td WIDTH="{int(anchoColuma)/int(columnasImagen)}" style="background-color: #FFFFFF"></td>\n"""
                continuar = False
            body += "\t\t\t\t</tr>\n"

        html = open(f"Proyecto1/templates/{nombreImagen}.html",'w+')
        html.write(head+body+bottom)

    def generarDoubleMirrorVarios(self,archivo):
        nombreImagen = self.listadeListaDeDatos[archivo][0].enviarData()[0]
        anchoColuma = self.listadeListaDeDatos[archivo][0].enviarData()[1]
        altoColuma = self.listadeListaDeDatos[archivo][0].enviarData()[2]
        filasImagen = self.listadeListaDeDatos[archivo][0].enviarData()[3]
        columnasImagen = self.listadeListaDeDatos[archivo][0].enviarData()[4]

        head = EncabezadoImagen()
        bottom = finalhtml()
        body = ""

        for i in range(int(filasImagen)-1,-1,-1):
            body += f"""\t\t\t\t<tr HEIGHT="{int(altoColuma)/int(filasImagen)}">\n"""
            for j in range(int(columnasImagen)-1,-1,-1):
                continuar = False
                for indice in range(0,len(self.listadeListaDeColores[archivo])):
                    if j == self.getNewColor(archivo,indice,0) and i == self.getNewColor(archivo,indice,1) and self.getNewColor(archivo,indice,2) == "TRUE":
                        body += f"""\t\t\t\t\t<td WIDTH="{int(anchoColuma)/int(columnasImagen)}" style="background-color: {self.getNewColor(archivo,indice,3)}"></td>\n"""
                        continuar = True
                        break
                if continuar == False:
                    body += f"""\t\t\t\t\t<td WIDTH="{int(anchoColuma)/int(columnasImagen)}" style="background-color: #FFFFFF"></td>\n"""
                continuar = False
            body += "\t\t\t\t</tr>\n"

        html = open(f"Proyecto1/templates/{nombreImagen}_DoubleMirror.html",'w+')
        html.write(head+body+bottom)


    
    def comprobando(self):
        return len(self.listadeListaDeColores[0])
    #print(len(self.listadeListaDeColores[0]))

    def generarMirrorXVarios(self,archivo):
        nombreImagen = self.listadeListaDeDatos[archivo][0].enviarData()[0]
        anchoColuma = self.listadeListaDeDatos[archivo][0].enviarData()[1]
        altoColuma = self.listadeListaDeDatos[archivo][0].enviarData()[2]
        filasImagen = self.listadeListaDeDatos[archivo][0].enviarData()[3]
        columnasImagen = self.listadeListaDeDatos[archivo][0].enviarData()[4]

        head = EncabezadoImagen()
        bottom = finalhtml()
        body = ""

        for i in range(0,int(filasImagen)):
            body += f"""\t\t\t\t<tr HEIGHT="{int(altoColuma)/int(filasImagen)}">\n"""
            for j in range(int(columnasImagen)-1,-1,-1):
                continuar = False
                for indice in range(0,len(self.listadeListaDeColores[archivo])):
                    if j == self.getNewColor(archivo,indice,0) and i == self.getNewColor(archivo,indice,1) and self.getNewColor(archivo,indice,2) == "TRUE":
                        body += f"""\t\t\t\t\t<td WIDTH="{int(anchoColuma)/int(columnasImagen)}" style="background-color: {self.getNewColor(archivo,indice,3)}"></td>\n"""
                        continuar = True
                        break
                if continuar == False:
                    body += f"""\t\t\t\t\t<td WIDTH="{int(anchoColuma)/int(columnasImagen)}" style="background-color: #FFFFFF"></td>\n"""
                continuar = False
            body += "\t\t\t\t</tr>\n"

        html = open(f"Proyecto1/templates/{nombreImagen}_MirrorX.html",'w+')
        html.write(head+body+bottom)

    def generarMirrorYVarios(self,archivo):
        nombreImagen = self.listadeListaDeDatos[archivo][0].enviarData()[0]
        anchoColuma = self.listadeListaDeDatos[archivo][0].enviarData()[1]
        altoColuma = self.listadeListaDeDatos[archivo][0].enviarData()[2]
        filasImagen = self.listadeListaDeDatos[archivo][0].enviarData()[3]
        columnasImagen = self.listadeListaDeDatos[archivo][0].enviarData()[4]

        head = EncabezadoImagen()
        bottom = finalhtml()
        body = ""

        for i in range(int(filasImagen)-1,-1,-1):
            body += f"""\t\t\t\t<tr HEIGHT="{int(altoColuma)/int(filasImagen)}">\n"""
            for j in range(0,int(columnasImagen)):
                continuar = False
                for indice in range(0,len(self.listadeListaDeColores[archivo])):
                    if j == self.getNewColor(archivo,indice,0) and i == self.getNewColor(archivo,indice,1) and self.getNewColor(archivo,indice,2) == "TRUE":
                        body += f"""\t\t\t\t\t<td WIDTH="{int(anchoColuma)/int(columnasImagen)}" style="background-color: {self.getNewColor(archivo,indice,3)}"></td>\n"""
                        continuar = True
                        break
                if continuar == False:
                    body += f"""\t\t\t\t\t<td WIDTH="{int(anchoColuma)/int(columnasImagen)}" style="background-color: #FFFFFF"></td>\n"""
                continuar = False
            body += "\t\t\t\t</tr>\n"

        html = open(f"Proyecto1/templates/{nombreImagen}_MirrorY.html",'w+')
        html.write(head+body+bottom)