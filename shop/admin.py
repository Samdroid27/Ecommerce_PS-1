from django.contrib import admin
from django.contrib import admin
from .models import Orders

# Register your models here.
from .models import Products, Contact
admin.site.register(Products)
admin.site.register(Contact)
admin.site.register(Orders)
