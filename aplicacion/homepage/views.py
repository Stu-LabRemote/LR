from smtplib import SMTPResponseException
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def principal(request):
    return render(request, 'aplicacion/homepage/plantillas/home/home.html')

def infoCL(request):
    return render(request, 'aplicacion/homepage/plantillas/PreLabs/infoCL.html')


def infoPI(request):
    return render(request, 'aplicacion/homepage/plantillas/PreLabs/infoPI.html')


def infoMR(request):
    return render(request, 'aplicacion/homepage/plantillas/PreLabs/infoMR.html')

def prueba(request):
    return render(request, 'plantillas/pruebas.html')
