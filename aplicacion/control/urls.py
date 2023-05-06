from django.urls import path
from aplicacion.control.views import controlCL, controlPI, controlMR, EnviarDatosCL, ReinicioCL

urlpatterns = [
    path('home/infoCL/controlCL/', controlCL, name='vista5'),
    path('home/infoPI/controlPI/', controlPI, name='vista6'),
    path('home/infoMR/controlMR/', controlMR, name='vista7'),

    #Enviar y eliminar datos
    path('EnviarDatosCL/', EnviarDatosCL, name='EnviarDatosCL'),
    path('ReinicioCL/<int:task_id>/', ReinicioCL, name='ReinicioCL'),
]
