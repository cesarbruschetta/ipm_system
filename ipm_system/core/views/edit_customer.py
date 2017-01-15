# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from ipm_system.core.forms import CustomerForm
from ipm_system.core.models import Customer


# Create your views here.
def edit_customer(request, id_customer):
    context = {}
    template = 'core/edit_customer.html'
    form_request = request.REQUEST
    form = None
    instance = None

    if id_customer == 'add':
        form = CustomerForm()
        is_edit = False
        context['title_page'] = 'Adição de Cliente'
    else:
        is_edit = True
        context['title_page'] = 'Edição de Cliente'
        try:
            instance = Customer.objects.get(pk=id_customer)
            form = CustomerForm(instance=instance)

        except Customer.DoesNotExist:
            form = CustomerForm()

    if 'submitted' in form_request.keys():
        if instance:
            form = CustomerForm(form_request, instance=instance)
        else:
            form = CustomerForm(form_request)

        if form.is_valid():
            form.save()

            redirect_url = reverse('view_customer', args=(form.instance.id,))
            return HttpResponseRedirect(redirect_url)

    context['customer'] = form.instance
    context['form'] = form
    context['is_edit'] = is_edit

    return render(request, template, context)
