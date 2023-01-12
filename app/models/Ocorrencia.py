from django.contrib.auth.models import User
from django.db import models
from app.models import *

class Ocorrencia(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    historico = models.TextField(default = "Nesta data, às HH:MM, o 9ºGBM foi acionado...",verbose_name="Histórico")
    data_preenchimento = models.DateTimeField(auto_now_add = True)
    ultima_atualizacao = models.DateTimeField(auto_now = True)
    data = models.DateTimeField()
    hora_chamada = models.TimeField()
    hora_no_local = models.TimeField()
    hora_termino = models.TimeField()
    nome_preenchedor = models.CharField(max_length=255)
    email_preenchedor = models.EmailField(max_length=255, null=False)
    
    posto_preenchedor = models.CharField(
        max_length=255,
        choices=POSTO_PREENCHEDOR_CHOICE,
        default="Sd BM"
        )
    
    meio_utilizado = models.CharField(
        max_length=255,
        choices=MEIO_UTILIZADO_CHOICES,
        default="Cicom"
    )

    situacao = models.CharField(
        max_length=250,
        choices=SITUACAO_CHOICES,
        default="Com intervenção",
        verbose_name="SITUAÇÃO"
    )
    matricula_preenchedor = models.IntegerField()
    
    tipo_de_utilizacao = models.CharField(
        max_length=255,
        choices=TIPO_DE_UTILIZACAO_CHOICES,
        default=""
        )
    
    def __str__(self):
        return '{} - {}' .format(self.nome_preenchedor, self.email_preenchedor)