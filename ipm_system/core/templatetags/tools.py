# -*- coding: utf-8 -*-
from django import template

import re

register = template.Library()


@register.filter(name='page_request_get')
def page_request_get(url_atual, page_number):
    url = re.sub(r'page=[0-9]+', '', url_atual)
    if '?' in url:
        return url + '&page=%s' % (page_number)
    else:
        return url + '?page=%s' % (page_number)


@register.filter(name='has_current')
def has_current(path, pattern):
    if re.search(pattern, path):
        return 'current'
    return ''
