# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=50, verbose_name=b'Categoria:')),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Nombre:')),
                ('last_name', models.CharField(max_length=50, verbose_name=b'Apellido:')),
                ('email', models.EmailField(max_length=50, verbose_name=b'E-mail')),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100, verbose_name=b'Titulo:')),
                ('contenido', ckeditor.fields.RichTextField()),
                ('resumen', models.CharField(max_length=300, verbose_name=b'Resumen')),
                ('imagen', models.ImageField(upload_to=b'blog')),
                ('fecha_publicacion', models.DateField()),
                ('slug', models.SlugField(editable=False)),
                ('categoria', models.ManyToManyField(to='blog.Categoria')),
            ],
        ),
    ]
