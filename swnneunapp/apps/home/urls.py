from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^$',
        views.Index.as_view(),
        name="index"
    ),
    #url que direccione a sub pagina quienes somos
    url(
        r'^nosotros/$',
        views.Nosotros.as_view(),
        name='nosotros'
    ),
    #url que direccionara a sub pagina servicios
    url(
        r'^services/$',
        views.Servicios.as_view(),
        name='servicios'
    ),
    #url que direccionara s sub pagina blog
    url(
        r'^blog/$',
        views.Blogger.as_view(),
        name='blog'
    ),
    #url que direccionara a sub pagina foro
    url(
        r'^foro/$',
        views.Foro.as_view(),
        name='foro'
    ),
    #url que direccionara a su pagina conatctenos
    url(
        r'^conatcto/$',
        views.ContactoView.as_view(),
        name='contacto'
    ),
]
