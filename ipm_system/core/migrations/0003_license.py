# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import encrypted_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_hardware'),
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license', encrypted_fields.fields.EncryptedTextField(default=b'')),
                ('customer', models.ForeignKey(to='core.Customer')),
                ('hardware', models.ForeignKey(to='core.Hardware')),
            ],
            options={
                'verbose_name': 'Licen\xe7a',
                'verbose_name_plural': 'Licen\xe7as',
            },
        ),
    ]
