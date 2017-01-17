# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ipm_system.core.models import Customer


def list_customer(request):
    template = 'core/list_customer.html'
    context = {}
    size = 5

    customers = Customer.objects.filter()

    if 'text_search' in request.GET.keys():
        text_search = request.GET.get('text_search')
        customers = customers.filter(name__icontains=text_search)

    customers_pag = Paginator(customers, size)
    page = request.GET.get('page')

    try:
        context['customers'] = customers_pag.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        context['customers'] = customers_pag.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        context['customers'] = customers_pag.page(customers_pag.num_pages)

    return render(request, template, context)
