from django.db import models


class CaidaLibre (models.Model):
    distancia = models.IntegerField(verbose_name='distancia',null=True)
    velocidad = models.FloatField(verbose_name='velocidad',null=True)
    tiempo = models.FloatField(verbose_name='tiempo',null=True)
    id = models.AutoField(primary_key=True,unique=True, verbose_name='id')

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.inp, self.ou, self.id)
    