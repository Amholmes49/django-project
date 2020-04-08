from django.shortcuts import render
from .models import Property, Tenant
# from django.contrib.auth.decorators import login_required

def properties_list(request):
    properties = Property.objects.all()
    return render(request, 'Rental_hub/properties_list.html', {'properties': properties })

def property_detail(request, pk):
    property = Property.objects.get(id=pk)
    return render(request, 'Rental_hub/property_detail.html', {'property': property })

def tenant_list(request):
    tenants = Tenant.objects.all()
    return render(request, 'Rental_hub/tenants_list.html', {'tenants': tenants })

def tenant_detail(request, pk):
    tenant = Tenant.objects.get(id=pk)
    return render(request, 'Rental_hub/tenant_detail.html', {'tenant': tenant})
