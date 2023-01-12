from django.forms import ModelForm
from django import forms
from app.models.Endereco import Endereco
from django.forms.widgets import *

class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields =  ['logradouro', 'cep', 'cidade', 'bairro',
        'uf', 'solicitante', 'fone', 'area_preservada',
        'caracteristica_local']
        widgets = {
               'carateristica_local': forms.RadioSelect(attrs={'class': "form-control"}),
               'area_preservada': forms.RadioSelect(),
               'data_chamada': NumberInput(attrs={'class': "form-control",'type': 'date'}),
               'data_no_local': NumberInput(attrs={'class': "form-control",'type': 'date'}),
               'data_termino': NumberInput(attrs={'class': "form-control",'type': 'date'})
        }
         