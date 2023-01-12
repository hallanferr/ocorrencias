from django.forms import ModelForm
from django import forms
from app.models.Ocorrencia import Ocorrencia
from django.forms.widgets import *


class OcorrenciaForm(ModelForm):
    class Meta:
        model = Ocorrencia
        fields =  ['historico', 'hora_chamada', 'hora_no_local', 'hora_termino', 'data',
        'nome_preenchedor', 'posto_preenchedor', 'meio_utilizado',
        'situacao','matricula_preenchedor','tipo_de_utilizacao']
        widgets = {
               'historico': forms.Textarea(attrs={'class': "form-control", "rows": 10}),
               'tipo_de_utilizacao': forms.RadioSelect(),
               'data' : NumberInput(attrs={'class': "form-control",'type': 'date'}),
               'hora_chamada': NumberInput(attrs={'class': "form-control",'type': 'time'}),
               'hora_no_local': NumberInput(attrs={'class': "form-control",'type': 'time'}),
               'hora_termino': NumberInput(attrs={'class': "form-control",'type': 'time'}),
               'meio_utilizado': forms.RadioSelect(attrs={'class': "form-control"}),
               'situacao': forms.RadioSelect(attrs={'class': "form-control"}),
               'nome_preenchedor': forms.TextInput(attrs={'class': "form-control"})  
           }