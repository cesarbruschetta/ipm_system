
# -*- encoding: utf-8 -*-
from django.shortcuts import render


def home(request):

    context = {
        'title_page': 'Home',
    }
    return render(request, 'core/index.html', context)
