# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='', max_length=255, verbose_name='Nome')),
                ('key', models.CharField(default='', max_length=255)),
                ('customer', models.ForeignKey(to='core.Customer')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Hardware',
                'verbose_name_plural': 'Hardwares',
            },
        ),
    ]
