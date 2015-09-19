# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name=b'nombre')),
                ('slug', models.SlugField(editable=False)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'titulo')),
                ('content', ckeditor.fields.RichTextField(verbose_name=b'contenido')),
                ('image', models.ImageField(upload_to=b'blog', verbose_name=b'imagen')),
                ('created', models.DateField(auto_now_add=True, verbose_name=b'Fecha de creacion')),
                ('views', models.PositiveIntegerField(default=0, verbose_name=b'visitas')),
                ('slug', models.SlugField(editable=False)),
                ('category', models.ManyToManyField(to='blog.Category', verbose_name=b'categoria(s)')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Entradas',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50, null=True, verbose_name=b'nombres')),
                ('last_name', models.CharField(max_length=50, null=True, verbose_name=b'apellidos')),
                ('email', models.EmailField(unique=True, max_length=50, verbose_name=b'E-mail')),
                ('avatar', models.ImageField(null=True, upload_to=b'users', blank=True)),
            ],
            options={
                'verbose_name': 'Suscripcion',
                'verbose_name_plural': 'Suscripciones',
            },
        ),
    ]
