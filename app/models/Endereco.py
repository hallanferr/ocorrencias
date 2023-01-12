from app.models import *
from django.db import models
from app.models.Ocorrencia import Ocorrencia
class Endereco(models.Model):
    ocorrencia = models.OneToOneField(Ocorrencia, on_delete=models.CASCADE)
    logradouro = models.CharField(max_length=255)
    cep = models.CharField(max_length=15)
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    uf = models.CharField(
        max_length=10,
        choices = ESTADOS_CHOICE
    )
    solicitante = models.CharField(max_length=255)
    fone = models.CharField(max_length=25, null = True)
    area_preservada = models.BooleanField(default=False)
    caracteristica_local = models.CharField(
        max_length=255,
        choices=CARACTERISTICA_LOCAL_CHOICES,
        default="Residencial"
        )