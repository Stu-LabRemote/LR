from smtplib import SMTPResponseException
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def registro(request):
    return render(request, 'aplicacion/user/plantillas/registro.html')


def login(request):
    return render(request, 'aplicacion/user/plantillas/login.html')
