# -*- coding: utf-8 -*-
from django.forms import ModelForm

from ipm_system.core.models import Hardware


class HardwareForm(ModelForm):
    class Meta:
        model = Hardware
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(HardwareForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs.update({'class': 'form-control'})
