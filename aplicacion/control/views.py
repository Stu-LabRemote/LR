from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import CaidaLibre
from django.urls import reverse


def controlCL(request):
    DatosCL = CaidaLibre.objects.all()
    context={
        "DatosCL":DatosCL[::-1]
    }
    return render(request, 'aplicacion/control/plantillas/control/controlCL.html', context)


def controlPI(request):
    return render(request, 'aplicacion/control/plantillas/control/controlPI.html')


def controlMR(request):
    return render(request, 'aplicacion/control/plantillas/control/controlMR.html')

def EnviarDatosCL(request):
    task_distancia=request.POST["DCL"]
    task_tiempo=request.POST["TCL"]
    task_id=request.POST["idCL"]
    DatosCL = CaidaLibre(distancia=task_distancia, tiempo=task_tiempo, id=task_id)
    DatosCL.save()
    return HttpResponseRedirect(reverse(controlCL))

def ReinicioCL(request, task_id):
    DatosCL= CaidaLibre.objects.filter(id=task_id)
    DatosCL.delete()
    return HttpResponseRedirect(reverse(controlCL))


#acciones
'''
def index_view (request):
    if request.POST:
        id = request.POST['DCL']
        encender()

    return render(request, 'controlCL.html')
    '''