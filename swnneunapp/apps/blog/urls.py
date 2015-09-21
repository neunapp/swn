from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^blog/$',
        views.IndexBlog.as_view(),
        name="blogger"
    ),
    url(
        r'^blog/(?P<slug>[-\w]+)/$',
        views.DetalleEntrada.as_view(),
        name="entrada"
    ),
   ]
