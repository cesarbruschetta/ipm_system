from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Hardware(models.Model):

    class Meta:
        app_label = 'core'
        verbose_name = u'Hardware'
        verbose_name_plural = u'Hardwares'
        ordering = ('name',)

    customer = models.ForeignKey('core.Customer')
    name = models.CharField(verbose_name="Nome",
                            default="", max_length=255)

    key = models.CharField(max_length=255, default='')
