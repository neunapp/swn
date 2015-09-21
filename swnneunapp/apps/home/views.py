# -*- encoding: utf-8 -*-
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail

from .models import Contacto

from .forms import ContactoForm


class Index(TemplateView):
    template_name = "home/index.html"


class Nosotros(TemplateView):
    template_name = "home/nosotros.html"


class Servicios(TemplateView):
    template_name = "home/servicios.html"


# formulario que registrar y enviar datos a un correo email
class ContactoView(FormView):
    template_name = "home/contacto.html"
    form_class = ContactoForm
    success_url = reverse_lazy('home_app:contacto')

    def form_valid(self, form):
        # recuperamos los valores para la tabla Contacto
        nombre = form.cleaned_data['name']
        email = form.cleaned_data['email']
        telefono = form.cleaned_data['phone']
        asunto = form.cleaned_data['business']
        horario = form.cleaned_data['horario']
        mensaje = form.cleaned_data['menssage']
        contacto = Contacto(
            name=nombre,
            email=email,
            phone=telefono,
            business=asunto,
            horario=horario,
            menssage=mensaje
        )
        send_mail(asunto, mensaje, email, ['neunapp.contacto@gmail.com'], fail_silently=False)
        contacto.save()
        return super(ContactoView, self).form_valid(form)
