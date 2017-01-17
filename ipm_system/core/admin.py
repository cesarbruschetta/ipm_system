from django.contrib import admin

# Register your models here.
from .models import Customer, Hardware, License


admin.site.register(Customer)
admin.site.register(Hardware)
admin.site.register(License)
