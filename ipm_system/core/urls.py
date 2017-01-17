from django.conf.urls import url

from .views import (home, list_customer, edit_customer,
                    view_customer, edit_hardware, download_license)

urlpatterns = [

    # CORE SITE
    url(r'^/?$', home, name='home'),

    url(r'^customer/$', list_customer, name='list_customer'),
    url(r'^customer/(?P<id_customer>\d+)/$',
        view_customer, name='view_customer'),
    url(r'^customer/(?P<id_customer>[add|\d]+)/edit$',
        edit_customer, name='edit_customer'),
    url(r'^customer/(?P<id_customer>\d+)/hardware/(?P<id_hardware>[add|\d]+)/edit$',
        edit_hardware, name='edit_hardware'),
    url(r'^customer/(?P<id_customer>\d+)/hardware/(?P<id_hardware>\d+)/download_license$',
        download_license, name='download_license'),
]
