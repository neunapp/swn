# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import *


class Index(TemplateView):
    template_name = "home/index.html"

class Nosotros(TemplateView):
	template_name = "home/nosotros.html"

class Servicios(TemplateView):
	template_name = "home/servicios.html"

class Blogger(TemplateView):
	template_name = "home/blogger.html"

class Foro(TemplateView):
	template_name = "home/foro.html"

class Contacto(CreateView):
	form_class = ContactoForm
	template_name = "home/contacto.html"
