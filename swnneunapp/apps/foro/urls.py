# -*- encoding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^foro$',
        views.RegisterQuestion.as_view(),
        name="foro"
    ),
    url(
        r'^foro/registrar-pregunta$',
        views.RegisterQuestion.as_view(),
        name="foro_registrar_pregunta"
    ),
    url(
        r'^foro/(?P<slug>[-\w]+)/$',
        views.RegisterAnswer.as_view(),
        name="foro_respuestas"
    ),
   ]