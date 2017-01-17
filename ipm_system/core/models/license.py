# -*- coding: utf-8 -*-
from django.db import models
from encrypted_fields import EncryptedTextField

import pickle


class License(models.Model):

    class Meta:
        app_label = 'core'
        verbose_name = 'Licença'
        verbose_name_plural = 'Licenças'

    customer = models.ForeignKey('core.Customer')
    hardware = models.ForeignKey('core.Hardware')
    license = EncryptedTextField(default='')

    def get_license(self):
        return pickle.loads(self.license)

    def __unicode__(self):
        return u"License - %s" % (self.hardware)
