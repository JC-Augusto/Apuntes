from Modulos.Errores import Errores
from Modulos.Token import Token
from Modulos.FuncionesAuxiliares import *
from prettytable import PrettyTable
import webbrowser

class Analizador: 
    def __init__(self):
        self.palabrasReservadas = ["Claves","Registros","imprimir","imprimirln","conteo","promedio","contarsi","datos","sumar","max","min","exportarReporte"]
        self.palabrasReservadas2 = ["Claves","Registros","imprimir","conteo","promedio","contarsi","datos","sumar","max","min","exportarReporte"]
        self.simbolosDeComentarios = ["'''", "#"]

        self.listaErroresLexicos = []
        self.listaErroresSintacticos = []
        self.listaTokens = []
        self.claves = []
        self.registros = []
        self.registro = []
        #datos automata
        self.estado = 0
        self.indexCadena = 0
        self.linea = 1
        self.columna = 1
        self.buffer = ''
        self.contadorAuxiliar = 0
        
        


        self.instruccion = ""
        self.datoInstruccion = ""
        self.datoDosInstruccion = ""

        self.cadenaImprimir = ""
        self.tituloDocumento = ""
        self.cadenaResult = ""


    def analizar(self, cadena):
        self.__init__()
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
            elif self.estado == 21:
                self.estado21(cadena[self.indexCadena])
            elif self.estado == 22:
                self.estado22(cadena[self.indexCadena])
            elif self.estado == 23:
                self.estado23(cadena[self.indexCadena])
            elif self.estado == 24:
                self.estado24(cadena[self.indexCadena])
            elif self.estado == 25:
                self.estado25(cadena[self.indexCadena])
            elif self.estado == 26:
                self.estado26(cadena[self.indexCadena])
            self.indexCadena += 1
        return self.cadenaResult

    def movimientoEstado(self, movColumna,movEstado, agregarBuffer):
        if movColumna == "reset":
            self.columna = 1
            self.linea += 1
        else: 
            self.columna += movColumna
        self.estado = movEstado
        if agregarBuffer == "":
            self.buffer = ""
        else:
            self.buffer += agregarBuffer


    def agregarToken(self, lexema, token):
        self.listaTokens.append(Token(lexema, token, self.linea, self.columna))

    def agregarErrorLexico(self, caracter): 
        self.listaErroresLexicos.append(Errores("Caracter "+str(caracter)+ " No reconocido en el lenguaje",self.linea, self.columna))

    def agregarErrorSintactico(self, caracter): 
        self.listaErroresSintacticos.append(Errores("El caracter: "+str(caracter)+ " No era el esperado en el lenguaje",self.linea, self.columna))
            
    def lexico(self,caracter):
        aceptacion = False
        if caracter.isalpha():
            aceptacion = True
        elif caracter.isdigit():
            aceptacion = True
        elif caracter == "\"":
            self.agregarToken(caracter,"comillas")
            aceptacion = True
        elif caracter == "=":
            self.agregarToken(caracter,"igual")
            aceptacion = True
        elif caracter == ";":
            self.agregarToken(caracter,"puntoComa")
            aceptacion = True
        elif caracter == "[":
            self.agregarToken(caracter,"corcheteAbierto")
            aceptacion = True
        elif caracter == "]":
            self.agregarToken(caracter,"corcheteCerrado")
            aceptacion = True
        elif caracter == "{":
            self.agregarToken(caracter,"llaveAbierta")
            aceptacion = True
        elif caracter == "}":
            aceptacion = True
        elif caracter == "(":
            self.agregarToken(caracter,"parentesisAbierto")
            aceptacion = True
        elif caracter == ")":
            aceptacion = True
        elif caracter == ",":
            aceptacion = True
        elif caracter == "#":
            aceptacion = True
        elif caracter == "'":
            aceptacion = True
        elif caracter == ".":
            aceptacion = True
        elif caracter in ["\t", " ", "\n", "\r"]:
            aceptacion = True
        else:
            aceptacion = False
        return aceptacion

    def estado0(self, caracter):
        if self.lexico(caracter) == True:
            if caracter.isalpha():
                self.movimientoEstado(1,1,caracter)
            elif caracter == "\n":
                self.movimientoEstado("reset",0,"")
            elif caracter == "\r":
                self.movimientoEstado(1,0,"")
            elif caracter == "\t":
                self.movimientoEstado(4,0,"")
            elif caracter == " ":
                self.movimientoEstado(1,0,"")
            elif caracter == "#":
                self.movimientoEstado(1,20,"")
            elif caracter == "'":
                self.movimientoEstado(1,21,caracter)
            else:
                self.agregarErrorSintactico(caracter)
                self.movimientoEstado(1,0,"")
        else:
            self.agregarErrorLexico(caracter)
            self.movimientoEstado(1,0,"")
    def estado1(self, caracter):
        if self.lexico(caracter) == True:
            if caracter.isalpha():
                self.movimientoEstado(1,1,caracter)
                if self.buffer in self.palabrasReservadas:
                    self.columna-=1
                    self.instruccion = self.buffer
                    if self.buffer == "imprimirln":
                        self.listaTokens.pop()
                        self.agregarToken(self.buffer,"palabraReservada")
                    else:
                        self.agregarToken(self.buffer,"palabraReservada")
                        self.columna+=1
            elif caracter == "=":   
                self.movimientoEstado(1,2,"")
            elif caracter == "(":
                self.movimientoEstado(1,3,"")
            elif caracter == " ":
                self.movimientoEstado(1,1,"")
            elif caracter == "\r":
                self.movimientoEstadoo(1,1,"")
            elif caracter == "\n":
                self.movimientoEstado("reset",1,"")
            else:
                self.agregarErrorSintactico(caracter)
                self.movimientoEstado(1,1,"")
        else:
            self.agregarErrorLexico(caracter)
            self.movimientoEstado(1,1,"")
    def estado2(self, caracter):
        if self.lexico(caracter) == True:
            if caracter == "[":
                self.movimientoEstado(1,4,"")
            elif caracter == " ":
                self.movimientoEstado(1,2,"")
            elif caracter == "\r":
                self.movimientoEstado(1,2,"")
            else:
                self.agregarErrorSintactico(caracter)
                self.movimientoEstado(1,2,"")
        else:
            self.agregarErrorLexico(caracter)
            self.movimientoEstado(1,2,"")
    def estado3(self, caracter):
        if self.lexico(caracter) == True:
            if caracter == ")":
                self.agregarToken(caracter,"parentesisCerrado")
                self.movimientoEstado(1,6,"")
            elif caracter == "\"":
                self.movimientoEstado(1,9,"")
            else:
                self.agregarErrorSintactico(caracter)
                self.movimientoEstado(1,3,"")
        else:
            self.agregarErrorLexico(caracter)
            self.movimientoEstado(1,3,"")
    def estado4(self, caracter):
        if self.lexico(caracter) == True:
            if caracter == "{":
                self.movimientoEstado(1,8,"")
            elif caracter == "\"":
                self.movimientoEstado(1,11,"")
            elif caracter == "\n":
                self.movimientoEstado("reset",4,"")
            elif caracter == "\t":
                self.movimientoEstado(4,4,"")
            elif caracter == "	":
                self.movimientoEstado(4,4,"")
            elif caracter == "\r":
                self.movimientoEstado(1,4,"")
            elif caracter == " ":
                self.movimientoEstado(1,4,"")
            else:
                self.agregarErrorLexico(caracter)
                self.movimientoEstado(1,4,"")
        else:
            self.agregarErrorLexico(caracter)
            self.movimientoEstado(1,4,"")
    def estado5(self, caracter):
        if self.lexico(caracter) == True:
            if caracter.isalpha():
                self.movimientoEstado(1,9,caracter)
            else:
                self.agregarErrorSintactico(caracter)
                self.movimientoEstado(1,5,"")
        else:
            self.agregarErrorLexico(caracter)
            self.movimientoEstado(1,5,"")
    def estado6(self, caracter):
        if self.lexico(caracter) == True:
            if caracter == ";":
                self.movimientoEstado(1,0,"")
                self.ejecutador(self.instruccion,"no necesita","")
            else:
                self.agregarErrorSintactico
                self.movimientoEstado(1,6,"")
        else:
            self.agregarErrorLexico(caracter)
            self.movimientoEstado(1,6,"")
    def estado7(self, caracter):
        if self.lexico(caracter) == True:
            if caracter.isalpha():
                self.movimientoEstado(1,11,caracter)
            else:
                self.agregarErrorSintactico(caracter)
                self.movimientoEstado(1,7,"")
        else:
            self.agregarErrorLexico(caracter)
            self.movimientoEstado(1,7,"")
    def estado8(self, caracter):
        if self.lexico(caracter) == True:
            if caracter.isdigit():
                self.movimientoEstado(1,12,caracter)
            elif caracter == "\"":
                self.movimientoEstado(1,25,"")
            elif caracter == " ":
                self.movimientoEstado(1,8,"")
            elif caracter == "\r":
                self.movimientoEstado(1,8,"")
            else:
                self.agregarErrorSintactico(caracter)
                self.movimientoEstado(1,8,"")
        else:
            self.agregarErrorLexico(caracter)
            self.movimientoEstado(1,8,"")
    def estado9(self, caracter):
        if caracter == "\"":
            self.columna -= 1
            self.agregarToken(self.buffer,"Cadena")
            self.columna +=1
            self.datoInstruccion = self.buffer
            self.agregarToken(caracter,"comillas")
            self.movimientoEstado(1,13,"")
        else:
            self.movimientoEstado(1,9,caracter)
    def estado10(self, caracter):
        if self.lexico(caracter) == True:
            if caracter == "]":
                self.movimientoEstado(1,0,"")
            elif caracter == "\n":
                self.movimientoEstado("reset",10,"")
            elif caracter == " ":
                self.movimientoEstado(1,10,"")
            elif caracter == "\r":
                self.movimientoEstado(1,10,"")
            elif caracter == "\t":
                self.movimientoEstado(4,10,"")
            elif caracter == "{":
                self.movimientoEstado(1,8,"")
            else:
                self.agregarErrorSintactico(caracter)
                self.movimientoEstado(1,10,"")
        else:
            self.agregarErrorLexico(caracter)
            self.movimientoEstado(1,10,"")
    def estado11(self, caracter):
        if caracter == "\"":
            self.columna -=1
            self.agregarToken(self.buffer,"cadena")
            self.claves.append(self.buffer)
            self.columna +=1
            self.agregarToken(caracter,"comillas")
            self.movimientoEstado(1,14,"")
        else:
            self.movimientoEstado(1,11,caracter)
    def estado12(self, caracter):
        if self.lexico(caracter) == True:
            if caracter.isdigit():
                self.movimientoEstado(1,12,caracter)
            elif caracter == ".":
                self.movimientoEstado(1,12,caracter)
            elif caracter == ",":
                self.columna -=1
                self.agregarToken(self.buffer,"digito")
                self.registro.append(self.buffer)
                self.columna +=1
                self.agregarToken(caracter,"coma")
                self.movimientoEstado(1,8,"")
            elif caracter == "}":
                self.columna -=1
                self.agregarToken(self.buffer,"digito")
                self.registro.append(self.buffer)
                self.registros.append(self.registro)
                self.registro = []
                self.columna +=1
                self.agregarToken(caracter,"llaveCerrada")
                self.movimientoEstado(1,10,"")
            else:
                self.agregarErrorLexico(caracter)
                self.movimientoEstado(1,12,"")
        else:
            self.agregarErrorLexico(caracter)
            self.movimientoEstado(1,12,"")
    def estado13(self, caracter):
        if self.lexico(caracter) == True:
            if caracter == ")":
                self.agregarToken(caracter,"parentesisCerrado")
                self.movimientoEstado(1,15,"")
            elif caracter == ",":
                self.agregarToken(caracter,"coma")
                self.movimientoEstado(1,16,"")
            else:
                self.agregarErrorSintactico(caracter)
                self.movimientoEstado(1,13,"")
        else:
            self.agregarErrorLexico(caracter)
            self.movimientoEstado(1,13,"")
    def estado14(self, caracter):
        if self.lexico(caracter) == True:
            if caracter == ",":
                self.agregarToken(caracter,"coma")
                self.movimientoEstado(1,17,"")
            elif caracter == "]":
                self.movimientoEstado(1,0,"")
            elif caracter == "\t":
                self.movimientoEstado(4,14,"")
            elif caracter == " ":
                self.movimientoEstado(1,14,"")
            elif caracter == "\r":
                self.movimientoEstado(1,14,"")
            elif caracter == "\n":
                self.movimientoEstado("reset",14,"")
            else:
                self.agregarErrorSintactico(caracter)
                self.movimientoEstado(1,14,"")
        else:
            self.agregarErrorLexico(caracter)
            self.movimientoEstado(1,14,"")
    def estado15(self, caracter):
        if self.lexico(caracter) == True:
            if caracter == ";":
                self.movimientoEstado(1,0,"")
                self.ejecutador(self.instruccion,self.datoInstruccion,"")
            elif caracter == "\n":
                self.movimientoEstado("reset",15,"")
            elif caracter == "\t":
                self.movimientoEstado(1,15,"")
            elif caracter == " ":
                self.movimientoEstado(1,15,"")
            elif caracter == "\r":
                self.movimientoEstado(1,15,"")
            else:
                self.agregarErrorSintactico(caracter)
                self.movimientoEstado(1,15,"")
        else:
            self.agregarErrorLexico(caracter)
            self.movimientoEstado(1,15,"")
    def estado16(self, caracter):
        if self.lexico(caracter) == True:
            if caracter.isdigit():
                self.movimientoEstado(1,18,caracter)
            elif caracter == " ":
                self.movimientoEstado(1,16,"")
            elif caracter == "\r":
                self.movimientoEstado(1,16,"")
            else:
                self.agregarErrorSintactico(caracter)
                self.movimientoEstado(1,16,"")
        else:
            self.agregarErrorLexico(caracter)
            self.movimientoEstado(1,16,"")
    def estado17(self, caracter):
        if self.lexico(caracter) == True:
            if caracter == "\"":
                self.movimientoEstado(1,11,"")
            elif caracter == "\n":
                self.movimientoEstado("reset",17,"")
            elif caracter == " ":
                self.movimientoEstado(1,17,"")
            elif caracter == "\r":
                self.movimientoEstado(1,17,"")
            elif caracter == "\t":
                self.movimientoEstado(4,17,"")
            else:
                self.agregarErrorSintactico(caracter)
                self.movimientoEstado(1,17,"")
        else:
            self.agregarErrorLexico(caracter)
            self.movimientoEstado(1,17,"")
    def estado18(self, caracter):
        if self.lexico(caracter) == True:
            if caracter.isdigit():
                self.movimientoEstado(1,18,caracter)
            elif caracter == ".":
                self.movimientoEstado(1,18,caracter)
            elif caracter == ")":
                self.columna -= 1
                self.agregarToken(self.buffer,"digito")
                self.columna +=1
                self.datoDosInstruccion = self.buffer
                self.agregarToken(caracter,"parentesisCerrado")
                self.movimientoEstado(1,19,"")
            else:
                self.agregarErrorSintactico(caracter)
                self.movimientoEstado(1,18,"")
        else:
            self.agregarErrorLexico(caracter)
            self.movimientoEstado(1,18,"")
    def estado19(self, caracter):
        if self.lexico(caracter) == True:
            if caracter == ";":
                self.movimientoEstado(1,0,"")
                self.ejecutador(self.instruccion,self.datoInstruccion,self.datoDosInstruccion)
            else:
                self.agregarErrorSintactico(caracter)
                self.movimientoEstado(1,19,"")
        else:
            self.agregarErrorLexico(caracter)
            self.movimientoEstado(1,19,"")


    def estado20(self, caracter):
        if caracter == "\n":
            self.movimientoEstado("reset",0,"")
        else:
            self.movimientoEstado(1,20,"")
    def estado21(self, caracter):
        if self.buffer in self.simbolosDeComentarios:
            self.indexCadena -=1
            self.columna -=1
            self.movimientoEstado(1,22,"")
            self.columna +=1
        else:
            if caracter == "'":
                self.movimientoEstado(1,21,caracter)
            else:
                self.agregarErrorLexico(self.buffer)
                self.movimientoEstado(1,0,"")
    def estado22(self, caracter):
        if caracter == "'":
            self.movimientoEstado(1,23,caracter)
        elif caracter == "\n":
            self.movimientoEstado("reset",22,"")
        else:
            self.movimientoEstado(1,22,"")
    def estado23(self, caracter):
        if self.buffer in self.simbolosDeComentarios:
            self.indexCadena -=1
            self.columna -=1
            self.movimientoEstado(1,0,"")
            self.columna +=1
        else:
            if caracter == "'":
                self.movimientoEstado(1,23,caracter)
            else:
                self.movimientoEstado(1,22,"")
    def estado24(self,caracter):
        if self.lexico(caracter) == True:
            if caracter.isalpha() or caracter.isdigit():
                self.movimientoEstado(1,25,caracter)
            else:
                self.agregarErrorSintactico(caracter)
                self.movimientoEstado(1,24,"")
        else:
            self.agregarErrorLexico(caracter)
            self.movimientoEstado(1,24,"")
    def estado25(self, caracter):
        if caracter == "\"":
            self.columna -=1
            self.agregarToken(self.buffer,"cadena")
            self.registro.append(self.buffer)
            self.columna +=1
            self.agregarToken(caracter,"comillas")
            self.movimientoEstado(1,26,"")
        else:
            self.movimientoEstado(1,25,caracter)
    def estado26(self, caracter):
        if self.lexico(caracter):
            if caracter == ",":
                self.movimientoEstado(1,8,"")
        else:
            self.agregarErrorLexico(caracter)
            self.movimientoEstado(1,26,"")
    



    def imprimirErroresLexicos(self):
        x = PrettyTable()
        x.field_names = ["Descripcion", "Fila", "Columna"]
        if len(self.listaErroresLexicos)==0:
            print('No hay errores lexicos')
        else:
            for i in self.listaErroresLexicos:
                x.add_row(i.enviarData())
            print(x)

    def imprimirTokens(self):
        x = PrettyTable()
        x.field_names = ["Lexema", "Token", "Fila", "Columna"]
        if len(self.listaTokens) == 0:
            print("NO hay tokens")
        else:
            for i in self.listaTokens:
                x.add_row(i.enviarData())
            print(x)

    def datos(self):
        cad = ""
        x = PrettyTable()
        x.field_names = self.claves
        if len(self.registros) == 0:
            print("NO hay tokens")
        else:
            for i in self.registros:
                x.add_row(i)
            cad += str(x)
        return cad

    def imprimirErroresSintacticos(self):

        x = PrettyTable()
        x.field_names = ["Descripcion", "Fila", "Columna"]
        if len(self.listaErroresSintacticos)==0:
            print('No hay errores sintacticos')
        else:
            for i in self.listaErroresSintacticos:
                x.add_row(i.enviarData())
            print(x)

    def conteo(self):
        x = len(self.registros)
        y = len(self.registros[0])
        return x*y


    def promedio(self,promediBuscado):
        promedio = len(self.registros)
        indice = self.claves.index(promediBuscado)
        suma = 0
        for registro in self.registros:
            suma += float(registro[indice])
        
        return (suma/promedio)

    def contarsi(self,buscarEN,buscado):
        indice = self.claves.index(buscarEN)
        contador = 0
        for registro in self.registros:
            if str(buscado) == registro[indice]:
                contador += 1
            else:
                pass
        return contador

    def sumar(self,buscado):
        indice = self.claves.index(buscado)
        suma = 0
        for registro in self.registros:
            suma += float(registro[indice])
        
        return suma
    def max(self,buscado):
        indice = self.claves.index(buscado)
        max = 0
        for registro in self.registros:
            dato = float(registro[indice])
            if dato > max:
                max = dato
            else:
                pass
        return max
    def min(self,buscado):
        indice = self.claves.index(buscado)
        min = float(self.registros[0][indice])
        for registro in self.registros:
            dato = float(registro[indice])
            if dato < min:
                min = dato
            else:
                pass
        return min

    def ejecutador(self,instruccion,datoInstruccion,dato2):
        if instruccion == "conteo":
            self.cadenaResult += (str(self.conteo())+"\n" )
            self.instruccion = ""
        elif instruccion == "promedio":
            self.cadenaResult += (str(self.promedio(datoInstruccion))+"\n" )
            self.instruccion == ""
        elif instruccion == "datos":
            self.cadenaResult += (str(self.datos())+"\n" )
            self.instruccion == ""
        elif instruccion == "sumar":
            self.cadenaResult += (str(self.sumar(datoInstruccion))+"\n" )
            self.instruccion == ""
        elif instruccion == "max":
            self.cadenaResult += (str(self.max(datoInstruccion))+"\n" )
            self.instruccion == ""
        elif instruccion == "min":
            self.cadenaResult += (str(self.min(datoInstruccion))+"\n" )
            self.instruccion == ""
        elif instruccion == "contarsi":
            self.cadenaResult += (str(self.contarsi(datoInstruccion,dato2))+"\n" )
            self.instruccion == ""
        elif instruccion == "imprimirln":
            self.cadenaResult += (datoInstruccion+"\n" )
        elif instruccion == "imprimir":
            self.cadenaResult += datoInstruccion
        elif instruccion == "exportarReporte":
            self.tituloDocumento = datoInstruccion
            self.exportarReporte(datoInstruccion)
            self.instruccion =""

    def EncabezadoHTML(self):
        inicioEncabezado = f"""
<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
</head>
<div class="row">
    <div class="col-md-6 offset-md-3">
        <div class = "table-responsive">
            <table class = "table table-striped table-bordered table-hover">
                <thead>
                    <th colspan = "{len(self.claves)}" style="background-color: rgb(22, 92, 45);"><p style="color:#e2e5e3";>{self.tituloDocumento}</p></th>
                    </tr>
                    <tr>
"""
        for clave in self.claves:
            inicioEncabezado += f"\t\t\t\t\t\t<th valign=\"middle\">{clave}</th>\n"

        finEncabezado = """
                    </tr>
                </thead>
        """
        return inicioEncabezado + finEncabezado

    def exportarReporte(self,titulo):
        head = self.EncabezadoHTML()
        bottom = finalhtml()
        body = ""
        
        for registro in self.registros:
            body += "\t\t\t\t\t<tr>\n"
            for dato in registro:
                body += f"\t\t\t\t\t\t<td>{dato}</td>\n" 
            body += "\t\t\t\t\t</tr>\n"
        html = open("templates/Reporte.html",'w+')
        html.write(head+body+bottom)

    def datosFinales(self):
        return self.cadenaResult

    def generarTablaErrores(self):
        head = EncabezadoErrores()
        bottom = finalhtml()
        body = ""
        for datos in self.listaErroresLexicos:
            body += f"""
                    <tr>
                        <td>{datos.enviarData()[0]}</td>
                        <td>{datos.enviarData()[1]}</td>                                            
                        <td>{datos.enviarData()[2]}</td>                        
                    </tr>"""   
        html = open("templates/ListaErroesLexicos.html",'w+')
        html.write(head+body+bottom)
    

    def generarTablaErroresSintacticos(self):
        head = EncabezadoErroresSintacticos()
        bottom = finalhtml()
        body = ""
        for datos in self.listaErroresSintacticos:
            body += f"""
                    <tr>
                        <td>{datos.enviarData()[0]}</td>
                        <td>{datos.enviarData()[1]}</td>                                            
                        <td>{datos.enviarData()[2]}</td>                        
                    </tr>"""   
        html = open("templates/ListaErroesSintacticos.html",'w+')
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
        html = open("templates/ListaTokens.html",'w+')
        html.write(head+body+bottom)
        
