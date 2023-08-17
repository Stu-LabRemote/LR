from django.urls import path

from aplicacion.user.views import registro, login


# urls de la aplicaccion
urlpatterns = [
    path('registro/', registro, name='vista2'),
    path('login/', login, name='vista3'),
]
