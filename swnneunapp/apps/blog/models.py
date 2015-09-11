from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    name = models.CharField('nombre', max_length=50, unique=True)
    slug = models.SlugField(editable=False)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Entry(models.Model):

    title = models.CharField('titulo', max_length=100)
    content = RichTextField('contenido')
    image = models.ImageField(upload_to='blog', verbose_name='imagen')
    created = models.DateField('Fecha de creacion', auto_now_add=True)
    category = models.ManyToManyField(Category, verbose_name='categoria(s)')
    views = models.PositiveIntegerField('visitas', default=0)
    slug = models.SlugField(editable=False)

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ["-created"]

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Entry, self).save(*args, **kwargs)


class Subscription(models.Model):
    first_name = models.CharField('nombres', max_length=50)
    last_name = models.CharField('apellidos', max_length=50)
    email = models.EmailField('E-mail', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Suscripcion'
        verbose_name_plural = 'Suscripciones'

    def __unicode__(self):
        return str(self.email)
