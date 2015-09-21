# -*- encoding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from apps.blog.models import Subscription
# Create your models here.

class Question(models.Model):
    username = models.ForeignKey(Subscription)    
    title = models.CharField('Titulo', max_length=50)
    question = models.CharField('Su Pregunta', max_length=300)
    date = models.DateField('Fecha de Creacion',auto_now_add=True)
    countanswer = models.PositiveIntegerField(default=0)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Question, self).save(*args, **kwargs)


class Answer(models.Model):
    username = models.ForeignKey(Subscription)
    question = models.ForeignKey(Question)
    date = models.DateField('Fecha de Creacion',auto_now_add=True)
    answer = models.CharField('Respuesta', max_length=300)

