# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse

from ipm_system.core.forms import HardwareForm
from ipm_system.core.models import Hardware, Customer


# Create your views here.
def edit_hardware(request, id_customer, id_hardware):
    context = {}
    template = 'core/edit_hardware.html'
    form_request = request.POST
    form = None
    instance = None

    try:
        obj_customer = Customer.objects.get(pk=id_customer)
    except Customer.DoesNotExist:
        raise Http404

    if id_hardware == 'add':
        form = HardwareForm()
        is_edit = False
        context['title_page'] = 'Adição de Cliente'
    else:
        is_edit = True
        context['title_page'] = 'Edição de Cliente'
        try:
            instance = Hardware.objects.get(pk=id_hardware,
                                            customer=obj_customer)
            form = HardwareForm(instance=instance)

        except Hardware.DoesNotExist:
            form = HardwareForm()

    if 'submitted' in form_request.keys():
        if instance:
            form = HardwareForm(form_request, instance=instance)
        else:
            form = HardwareForm(form_request)

        if form.is_valid():
            form.instance.customer = obj_customer
            form.save()

            redirect_url = reverse('view_customer', args=(obj_customer.id,))
            return HttpResponseRedirect(redirect_url)

    context['hardware'] = form.instance
    context['customer'] = obj_customer
    context['form'] = form
    context['is_edit'] = is_edit

    return render(request, template, context)
