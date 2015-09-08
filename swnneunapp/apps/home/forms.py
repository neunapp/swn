# -*- encoding: utf-8 -*-
from django import forms
from .models import *


class ContactoForm(forms.Form):
    name = forms.CharField(
        label='Su Nombre:',
        max_length='8')
    email = forms.EmailField(label='Su E-mail:')
    phone = forms.CharField(label='Su Telefono o Celular', required=False)
    business = forms.CharField(label='Asuto')
    horario = forms.CharField(label='¿En que horarios podemos contactarlo ?', required=False)
    menssage = forms.CharField(label='¿Cual es su Conslta?', widget=forms.Textarea(attrs={'cols':80,'rows':30}))
    
    def clean_menssage(self):
        mensaje = self.cleaned_data['menssage']
        num_palabras = len(mensaje.split())
        if num_palabras<4:
            raise forms.ValidationError("La consulta no es valida: Demasiado Corto, El sistema no entiende le mensaje :(")
        return mensaje
