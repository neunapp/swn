# -*- encoding: utf-8 -*-
from django.db import models
# Create your models here.

class Contacto(models.Model):
    name = models.CharField('nombre', max_length=50)
    email = models.EmailField('E-mail')
    phone = models.CharField('Telefono', max_length=50)
    business = models.CharField('Asunto', max_length=50)
    horario = models.CharField('Sugiera una Hora Para Contactarlo', max_length=50)
    menssage = models.CharField('¿Cual es tu Consulta?', max_length=200)

class Cliente(models.Model):
    company = models.CharField('Empresa', max_length=50)
    link = models.URLField()
    image = models.ImageField()
    description = models.CharField('Descripcion', max_length=50)
    
