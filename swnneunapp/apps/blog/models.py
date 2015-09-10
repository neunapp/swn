from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField('Categoria:', max_length=50, unique=True)

class Entrada(models.Model):

     titulo = models.CharField('Titulo:', max_length=100)
     contenido = RichTextField()
     resumen = models.CharField('Resumen', max_length=300)
     imagen = models.ImageField(upload_to='blog')
     fecha_publicacion = models.DateField()
     categoria = models.ManyToManyField(Categoria)
     slug = models.SlugField(editable=False)

     def __unicode__(self):
         return self.titulo

     def save(self, *args, **kwargs):
         if not self.id:
             self.slug = slugify(self.titulo)
         super(Entrada, self).save(*args, **kwargs)

class Suscripcion(models.Model):
    name = models.CharField('Nombre:', max_length=50)
    last_name = models.CharField('Apellido:', max_length=50)
    email = models.EmailField('E-mail', max_length=50)
