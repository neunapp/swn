from django import forms
from .models import *


class SucripcionForm(forms.Form):
    name = forms.CharField(
        label='Su Nombre:',
        max_length='50', required=False)
    last_name = forms.CharField(
        label='Su Apellido:',
        max_length='50', required=False)
    email = forms.EmailField(label='Su E-mail:')
    print '================ entro al formulario form ==============='