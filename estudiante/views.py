from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

# Create your views here.


def saludar(request):
    return HttpResponse(f'Hola mi nombre es Ricardo y la hora es {datetime.now()}')


def fechahoy(request):
    dia_de_hoy = datetime.now()
    return HttpResponse(f'<br><i> esta es otra vista mas criminal </i></br> {dia_de_hoy}')

# parametros pasados por url


def mi_nombre(request, nombre):

    return HttpResponse(f'Mi nombre es:  {nombre}')


# Probando template
