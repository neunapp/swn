from django.contrib import admin

# Register your models here.
from .models import Contacto, Cliente

admin.site.register(Contacto)
admin.site.register(Cliente)