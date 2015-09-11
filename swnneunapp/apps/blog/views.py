from django.views.generic.edit import FormView, FormMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView

from .models import Entry, Category, Subscription

from .forms import SuscripcionForm


class IndexBlog(FormView):
    template_name = 'blog/index.html'
    form_class = SuscripcionForm
    success_url = reverse_lazy('blog_app:blogger')

    def get_context_data(self, **kwargs):
        context = super(IndexBlog, self).get_context_data(**kwargs)
        context['entrys'] = Entry.objects.all()
        context['categorys'] = Category.objects.order_by('name')
        return context

    def form_valid(self, form):
        first_name = form.cleaned_data['name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        subscription = Subscription(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        subscription.save()
        return super(IndexBlog, self).form_valid(form)


class DetalleEntrada(FormMixin, DetailView):
    model = Entry
    form_class = SuscripcionForm
    template_name = 'blog/detalle.html'

    def get_success_url(self):
        return reverse_lazy('blog_app:blogger')

    #llamamos al metodo index blg para almacenar sucribciones
    def get_context_data(self, **kwargs):
        context = super(DetalleEntrada, self).get_context_data(**kwargs)
        #enviamos el formulario
        context['form'] = self.get_form()
        context['entrys'] = Entry.objects.all()
        context['categorys'] = Category.objects.order_by('name')
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
        first_name = form.cleaned_data['name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        subscription = Subscription(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        subscription.save()
        return super(DetalleEntrada, self).form_valid(form)
