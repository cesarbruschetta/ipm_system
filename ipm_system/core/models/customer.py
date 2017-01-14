from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Customer(models.Model):

    class Meta:
        app_label = 'core'
        verbose_name = u'Cliente'
        verbose_name_plural = u'Clientes'
        ordering = ('name',)

    title = models.CharField(verbose_name="Nome",
                             default="", max_length=255)

    