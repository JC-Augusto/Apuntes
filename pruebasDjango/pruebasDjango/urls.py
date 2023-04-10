"""pruebasDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pruebasDjango.views import bienvenida, bienvenidaColor, categoriaEdad, momentoActual, contenidoHTML, primeraPlantilla, primeraPlantillaParametros


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pruba/', bienvenida),
    path('otraPrueba/', bienvenidaColor),
    path('xd/<int:edad>',categoriaEdad),
    path('hora/', momentoActual),
    path('pruebaHTML/<nombre>/<int:edad>', contenidoHTML),
    path('primeraPlantilla/',primeraPlantilla),
    path('primeraPlantillaParametros/',primeraPlantillaParametros),
]
    
