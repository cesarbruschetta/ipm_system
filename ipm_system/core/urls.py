from django.conf.urls import url

from .views import home

urlpatterns = [

    # CORE SITE
    url(r'^/?$', home, name='home'),

]
