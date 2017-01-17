from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import (
    MultipleObjectsReturned, ObjectDoesNotExist)

from ipm_system.core.utils import gera_license

import hashlib
import pickle


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

    def __unicode__(self):
        return u"Hardware %s - %s" % (self.name, self.customer)

    def save(self, *args, **kwargs):
        if not self.key:
            h = hashlib.md5()
            h.update(
                self.__unicode__().encode('utf-8')
            )

            self.key = h.hexdigest()
        super(Hardware, self).save(*args, **kwargs)

    def get_license(self):

        try:
            license = self.license_set.get()
        except MultipleObjectsReturned:
            lics = self.license_set.filter()
            license = lics[0]
            for c in lics[1:]:
                c.delete()

        except ObjectDoesNotExist:
            license = self.license_set.create(customer=self.customer,
                                              hardware=self)
            license.license = pickle.dumps(gera_license())
            license.save()

        return license
