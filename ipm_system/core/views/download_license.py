# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from ipm_system.core.models import Hardware, Customer

from StringIO import StringIO


# Create your views here.
def download_license(request, id_customer, id_hardware):

    try:
        obj_customer = Customer.objects.get(pk=id_customer)
    except Customer.DoesNotExist:
        raise Http404

    try:
        obj_hardware = Hardware.objects.get(pk=id_hardware,
                                            customer=obj_customer)
    except Hardware.DoesNotExist:
        raise Http404

    obj = obj_hardware.get_license()

    myfile = StringIO()
    myfile.write(obj.get_license())

    response = HttpResponse(content_type='application/force-download')
    response['Content-Disposition'] = u'attachment; filename="licenca_%s.lic"' % (
        obj_hardware.name.replace(' ', '_')
    )
    response.write(myfile.getvalue())

    return response
