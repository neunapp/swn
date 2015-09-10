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
    #url que direccionara a su pagina conatctenos
    url(
        r'^conatcto/$',
        views.ContactoView.as_view(),
        name='contacto'
    ),
]
