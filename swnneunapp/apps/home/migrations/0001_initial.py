# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'nombre')),
                ('email', models.EmailField(max_length=254, verbose_name=b'E-mail')),
                ('phone', models.CharField(max_length=50, verbose_name=b'Telefono')),
                ('business', models.CharField(max_length=50, verbose_name=b'Asunto')),
                ('horario', models.CharField(max_length=50, verbose_name=b'Sugiera una Hora Para Contactarlo')),
                ('menssage', models.CharField(max_length=200, verbose_name=b'\xc2\xbfCual es tu Consulta?')),
            ],
        ),
    ]
