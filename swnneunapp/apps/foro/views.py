# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView
from django.views.generic.edit import FormView, FormMixin
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView

from django.utils import timezone

from .models import *

from apps.blog.models import Subscription

from .forms import *

# Create your views here.

class RegisterQuestion(FormView):
    template_name = "foro/index.html"
    form_class = RegisterQuestionForm
    success_url = reverse_lazy('foro_app:foro')

    def get_context_data(self, **kwargs):
        context = super(RegisterQuestion, self).get_context_data(**kwargs)
        context['questions'] = Question.objects.order_by('date')
        return context

    def form_valid(self, form):
        #recuperamos los valores que necesitamos almacenar
        user = form.cleaned_data['email']
        name = form.cleaned_data['apelativo']
        imagen = form.cleaned_data['image']
        #variable para almacenr suscrito
        usuario = 0
        #verificamos si el usuario existe
        if Subscription.objects.filter(email=user).count()>0:
            usuario = Subscription.objects.get(email=user)
        else:

            #registramos como nuevo suscrito
            suscripcion = Subscription(
                            first_name=name,
                            last_name=name,
                            email=user, 
                            avatar=imagen     
                            )
            suscripcion.save()
            #recueoramos el nuevo usuario
            usuario = Subscription.objects.get(email=user)

        titulo = form.cleaned_data['title']
        pregunta = form.cleaned_data['question']
        fecha = timezone.now()

        question = Question(
                     username=usuario,
                     title=titulo,
                     question=pregunta,
                     date=fecha
                            )
        question.save()
        return super(RegisterQuestion,self).form_valid(form)

class RegisterAnswer(FormMixin, DetailView):
    model = Question
    form_class = RegisterAnswerForm
    template_name = "foro/respuestas.html"

    def get_success_url(self):
       return reverse_lazy('foro_app:foro')

    #primero recuperamos a la lista de respuestas
    def get_context_data(self, **kwargs):
       context = super(RegisterAnswer, self).get_context_data(**kwargs)
       context['form'] = self.get_form()
       #obtenemos la pregunta
       pregunta = self.object
       #recuperams la lista de preguntas
       context['answers'] = Answer.objects.filter(question=pregunta)
       return context

    def post(self, request, *args, **kwargs):
        # get_object() es el parametro matricula q se psa por url
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
       #recuperamos el email del usaurio
       email = form.cleaned_data['email']
       #creamos una variable apra usuario
       usuario = Subscription.objects.filter(email=email).count()
       #verificamos si el usaurio es nuevo
       if usuario >=1:
            print 'el usuario ya esxiste'
            usuario = Subscription.objects.get(email=email)
       else:
        #si no existe lo guardamos como nuevo
            suscripcion = Subscription(
                          email=email,
                          first_name=email,
                          last_name=email,
            )
            suscripcion.save()
            print '############El usuario no existe'
            usuario = Subscription.objects.get(email=email)

       question = self.object
       #actualizamso la cantidad de preguntas respondidas
       question.countanswer= question.countanswer+1
       #recuperamos la respuesta
       answer = form.cleaned_data['answer']

       respuesta = Answer(
		            username=usuario,
                    question=question,
		            answer=answer,
		)
       respuesta.save()
       #actualizamos la pregunta
       question.save()
       return super(RegisterAnswer,self).form_valid(form)

        

