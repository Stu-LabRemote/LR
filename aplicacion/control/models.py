from django.db import models


class CaidaLibre (models.Model):
    inp = models.IntegerField(verbose_name='inp',null=True)
    ou = models.IntegerField(verbose_name='ou',null=True)
    id = models.AutoField(primary_key=True,unique=True, verbose_name='id')

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.inp, self.ou, self.id)
    