# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='', max_length=255, verbose_name='Nome')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
