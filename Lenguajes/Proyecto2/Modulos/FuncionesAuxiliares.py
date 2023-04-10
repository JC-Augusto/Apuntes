from tkinter import*
from tkinter import filedialog
import imgkit

def rutaArchivo() -> str:
    """Devuelve la ruta del archivo"""
    archivo = filedialog.askopenfilename(filetypes=(("Archivos lfp","*.lfp"),("Archivos de texto","*.txt")), title="Seleccione el archivo")
    return archivo

def leerArchivo(ruta):
    archivo = open(ruta, 'r')
    contenido = archivo.read()
    archivo.close()
    return contenido

def escribirArchivo(ruta, contenido):
    archivo = open(ruta, 'w')
    archivo.write(contenido)
    archivo.close()


def finalhtml():
    pie = """
            </table>
        </div>
    </div>
</div>"""
    return pie

def EncabezadoErrores():
    encabezado = """
<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
</head>
<div class="row">
    <div class="col-md-6 offset-md-3">
        <div class = "table-responsive">
            <table class = "table table-striped table-bordered table-hover">
                <thead>
                    <th colspan = "3" style="background-color: rgb(22, 92, 45);"><p style="color:#e2e5e3";>LISTA ERRORES LEXICOS</p></th>
                    </tr>
                    <tr>
                        <th valign="middle">Descripcion</th>
                        <th valign="middle">Fila</th>
                        <th valign="middle">Columna</th>
                    </tr>
                </thead>
"""
    return encabezado

def EncabezadoErroresSintacticos():
    encabezado = """
<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
</head>
<div class="row">
    <div class="col-md-6 offset-md-3">
        <div class = "table-responsive">
            <table class = "table table-striped table-bordered table-hover">
                <thead>
                    <th colspan = "3" style="background-color: rgb(22, 92, 45);"><p style="color:#e2e5e3";>LISTA ERRORES SINTACTICOS</p></th>
                    </tr>
                    <tr>
                        <th valign="middle">Descripcion</th>
                        <th valign="middle">Fila</th>
                        <th valign="middle">Columna</th>
                    </tr>
                </thead>
"""
    return encabezado

def EncabezadoTokens():
    encabezado = """
<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
</head>
<div class="row">
    <div class="col-md-6 offset-md-3">
        <div class = "table-responsive">
            <table class = "table table-striped table-bordered table-hover">
                <thead>
                    <th colspan = "4" style="background-color: rgb(22, 92, 45);"><p style="color:#e2e5e3";>LISTA TOKENS</p></th>
                    </tr>
                    <tr>
                        <th valign="middle">Lexema</th>
                        <th valign="middle">Token</th>
                        <th valign="middle">Fila</th>
                        <th valign="middle">Columna</th>
                    </tr>
                </thead>
"""
    return encabezado

