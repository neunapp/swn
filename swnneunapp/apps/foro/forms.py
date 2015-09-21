# -*- encoding: utf-8 -*-
from django import forms
from .models import *

from django.contrib.auth import authenticate


class RegisterQuestionForm(forms.Form):
    email = forms.EmailField(
        label='Su Email',
        max_length='50',
        required=True,
    )
    title = forms.CharField(
        label='Titulo',
        max_length='50', required=True)
    question = forms.CharField(label='Pregunta:',
        max_length='300',
        widget=forms.Textarea(attrs={'cols':80,'rows':30}),
        required=False,
    )
    apelativo = forms.CharField(
        label='Apelativo',
        max_length='10', required=False)
    image = forms.ImageField(required=False)

class RegisterAnswerForm(forms.Form):
    email = forms.EmailField(label='Su E-mail:',
        max_length='70',
        required=False,
        )
    answer = forms.CharField(label='Su Respuesta', max_length='300', widget=forms.Textarea(attrs={'cols':80,'rows':30}))