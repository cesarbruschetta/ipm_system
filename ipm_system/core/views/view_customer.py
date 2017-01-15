# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ipm_system.core.models import Customer


def view_customer(request, id_customer):
    context = {}
    template = 'core/view_customer.html'
    size = 10

    try:
        obj_customer = Customer.objects.get(pk=id_customer)
    except Customer.DoesNotExist:
        raise Http404

    hardwares = obj_customer.get_hardwares()

    if 'text_search' in request.REQUEST.keys():
        text_search = request.REQUEST.get('text_search')
        hardwares = hardwares.filter(name__icontains=text_search)

    hardwares_pag = Paginator(hardwares, size)
    page = request.GET.get('page')

    try:
        context['hardwares'] = hardwares_pag.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        context['hardwares'] = hardwares_pag.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        context['hardwares'] = hardwares_pag.page(hardwares_pag.num_pages)

    context['customer'] = obj_customer

    return render(request, template, context)
