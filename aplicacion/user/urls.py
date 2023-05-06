from django.urls import path

from aplicacion.user.views import registro, loguear

# urls de la aplicaccion
urlpatterns = [
    path('registro/', registro, name='vista2'),
    path('loguear/', loguear, name='vista3'),
]
