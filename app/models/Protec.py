"""from app.models import *
from django.db import models


class Protec(models.Model):
    ocorrencia = models.ForeignKey(Ocorrencia, related_name= 'ocorrencia', on_delete=models.CASCADE)
    tipo = models.CharField(
        max_length=50,
        choices = SISTEMA_PROTEC_CHOICES
    )
    utilizado = models.CharField(
        max_length=50,
        choices = SIM_NAO_CHOICES
    )
    
    def __str__(self):
        return '{}' .format(self.tipo)"""