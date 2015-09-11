from django import forms


class SuscripcionForm(forms.Form):
    first_name = forms.CharField(
        label='Su Nombre',
        max_length='70',
        required=False,
    )
    last_name = forms.CharField(
        label='Su Apellido',
        max_length='70',
        required=False
    )
    email = forms.EmailField(label='Su E-mail')
