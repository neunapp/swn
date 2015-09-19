# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True, verbose_name=b'Fecha de Creacion')),
                ('answer', models.CharField(max_length=300, verbose_name=b'Respuesta')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'Titulo')),
                ('question', models.CharField(max_length=300, verbose_name=b'Su Pregunta')),
                ('date', models.DateField(auto_now_add=True, verbose_name=b'Fecha de Creacion')),
                ('countanswer', models.PositiveIntegerField(default=0)),
                ('slug', models.SlugField(editable=False)),
                ('username', models.ForeignKey(to='blog.Subscription')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='foro.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='username',
            field=models.ForeignKey(to='blog.Subscription'),
        ),
    ]
