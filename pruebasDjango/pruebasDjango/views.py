
from django import http
from django.http import HttpResponse
from django.http.request import HttpHeaders
import datetime
from django.template import Template,Context

# request Sirve para realizar peticiones
# HttpResponse: Para enviar la respuesta usando el protocolo HTTP

#esto es una vista
def bienvenida(request): #pasamos un objeto de tipo request como primer argumento de la funcion vista de bienvenida
    return HttpResponse("Esto es una preuba") # 

def bienvenidaColor(request): #
    return HttpResponse("<h1 style= 'color: blue;'> esto es otra prueba </h1>")

def categoriaEdad(request,edad):
    if edad > 60:
        categoria = "Tercera edad"
    else:
        categoria = "adultes"
    resultado = f"<h1> usted esta en la {categoria}" 
    return HttpResponse(resultado)

def momentoActual(request):
    respuesta = f"Mometo Actual: {datetime.datetime.now()}"
    return HttpResponse(respuesta)

def contenidoHTML(request, nombre,edad):
    contenido = f"""
    <html>
    <body>
    <p>Nombre: {nombre} edad: {edad}</p>
    </body>
    </html>
    """

    return HttpResponse(contenido)

def primeraPlantilla(request):

    #Abrimos el documento que contiene la plantilla
    plantillaExterna = open( "C:/Users/jca19/Desktop/Proyects/Apuntes/pruebasDjango/pruebasDjango/Plantillas/plantilla.html")

    #Cargamos la plantilla en una variable de tipo "Template"
    template = Template(plantillaExterna.read())
    plantillaExterna.close()

    #Creamos un contexto en el cual se le puedan pasar parametros que seran consumidos por la plantilla
    contexto = Context()

    documento = template.render(contexto)
    return HttpResponse(documento)

def primeraPlantillaParametros(request):
    nombrePersonaje = "JCA"
    fechaActual = datetime.datetime.now()
    #Abrimos el documento que contiene la plantilla
    plantillaExterna = open( "C:/Users/jca19/Desktop/Proyects/Apuntes/pruebasDjango/pruebasDjango/Plantillas/plantillaParametros.html")

    #Cargamos la plantilla en una variable de tipo "Template"
    template = Template(plantillaExterna.read())
    plantillaExterna.close()

    #Creamos un contexto en el cual se le puedan pasar parametros que seran consumidos por la plantilla
    contexto = Context({"nickName": nombrePersonaje, "fecha": fechaActual})

    documento = template.render(contexto)
    return HttpResponse(documento)
