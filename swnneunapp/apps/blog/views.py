from django.shortcuts import render
from django.views.generic.edit import FormView, FormMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView

from .models import Entrada, Categoria, Suscripcion

from .forms import SucripcionForm
# Create your views here.

#creamos el view para la url index_blog
class IndexBlog(FormView):
    template_name = 'blog/index.html'
    form_class = SucripcionForm
    success_url = reverse_lazy('blog_app:blogger')

    def get_context_data(self, **kwargs):
        context = super(IndexBlog, self).get_context_data(**kwargs)
        #especificamos la cantidad de entradas que aparecran
        context['entradas'] = Entrada.objects.order_by('fecha_publicacion')[:6]
        context['categorias'] = Categoria.objects.order_by('nombre')
        return context

    def form_valid(self, form):
        nombre = form.cleaned_data['name']
        apellido = form.cleaned_data['last_name']
        e_mail = form.cleaned_data['email']
        suscripcion = Suscripcion(
            name=nombre,
            last_name=apellido,
            email=e_mail,
        ) 
        suscripcion.save()
        return super(IndexBlog, self).form_valid(form)


class DetalleEntrada(FormMixin, DetailView):
    model = Entrada
    form_class = SucripcionForm
    template_name = 'blog/detalle.html'

    def get_success_url(self):
        return reverse_lazy('blog_app:blogger'
        )
    
    #llamamos al metodo index blg para almacenar sucribciones
    def get_context_data(self, **kwargs):
        context = super(DetalleEntrada, self).get_context_data(**kwargs)
        #enviamos el formulario
        context['form'] = self.get_form()
        #especificamos la cantidad de entradas que aparecran
        context['entradas'] = Entrada.objects.order_by('fecha_publicacion')[:6]
        context['categorias'] = Categoria.objects.order_by('nombre')
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
        nombre = form.cleaned_data['name']
        apellido = form.cleaned_data['last_name']
        e_mail = form.cleaned_data['email']
        suscripcion = Suscripcion(
            name=nombre,
            last_name=apellido,
            email=e_mail,
        ) 
        suscripcion.save()
        return super(DetalleEntrada, self).form_valid(form)