# -*- coding: utf-8 -*-
from django.forms import ModelForm

from ipm_system.core.models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs.update({'class': 'form-control'})
