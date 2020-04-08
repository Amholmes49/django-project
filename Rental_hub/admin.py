from django.contrib import admin

# Register your models here.
from .models import Property, Tenant

admin.site.register(Property)
admin.site.register(Tenant)