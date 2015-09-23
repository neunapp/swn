# -*- encoding: utf-8 -*-
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail

from apps.foro.models import Question

from .models import Contacto

from .forms import ContactoForm

from apps.blog.models import Entry, Subscription
from apps.blog.forms import SuscripcionForm


class Index(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['entrys'] = Entry.objects.order_by('created')[:3]
        return context

class Nosotros(FormView):
    template_name = 'home/nosotros.html'
    form_class = SuscripcionForm
    success_url = reverse_lazy('home_app:nosotros')

    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        if Subscription.objects.filter(email=email).count()==0:
            subscription = Subscription(
                first_name=first_name,
                last_name=last_name,
                email=email,
            )
            subscription.save()
        return super(Nosotros, self).form_valid(form)


class Servicios(TemplateView):
    template_name = "home/servicios.html"


# formulario que registrar y enviar datos a un correo email
class ContactoView(FormView):
    template_name = "home/contacto.html"
    form_class = ContactoForm
    success_url = reverse_lazy('home_app:contacto')

    def get_context_data(self, **kwargs):
        context = super(ContactoView, self).get_context_data(**kwargs)
        context['questions'] = Question.objects.order_by('date')[:6]
        return context

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
