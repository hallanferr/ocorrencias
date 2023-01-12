from django.forms import ModelForm
from django import forms
from app.models.Protec import Protec
from django.forms.widgets import *


class ProtecForm(ModelForm):
    class Meta:
        model = Protec
        fields =  ['tipo', 'utilizado']
        widgets = {
               'utilizado': forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),
               'tipo': forms.CheckboxSelectMultiple(attrs={'class':'form-control'})
        }
        