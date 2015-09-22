# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=50, verbose_name=b'Empresa')),
                ('link', models.URLField()),
                ('image', models.ImageField(upload_to=b'')),
                ('description', models.CharField(max_length=50, verbose_name=b'Descripcion')),
            ],
        ),
    ]
