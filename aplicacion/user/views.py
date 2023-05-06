from smtplib import SMTPResponseException
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def registro(request):
    return render(request, 'aplicacion/user/plantillas/registro.html')


def loguear(request):
    return render(request, 'aplicacion/user/plantillas/loguear.html')
