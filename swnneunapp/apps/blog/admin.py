from django.contrib import admin
from .models import Entrada, Categoria, Suscripcion
# Register your models here.

admin.site.register(Entrada)
admin.site.register(Categoria)
admin.site.register(Suscripcion)