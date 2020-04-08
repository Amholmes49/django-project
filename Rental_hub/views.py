from django.shortcuts import render, redirect
from .models import Property, Tenant
from .forms import PropertyForm, TenantForm
# from django.contrib.auth.decorators import login_required

def properties_list(request):
    properties = Property.objects.all()
    return render(request, 'Rental_hub/properties_list.html', {'properties': properties })

def property_detail(request, pk):
    property = Property.objects.get(id=pk)
    return render(request, 'Rental_hub/property_detail.html', {'property': property })

def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            property = form.save()
            return redirect('property_detail', pk=property.pk)
    else:
        form = PropertyForm()
    return render(request, 'Rental_hub/property_form.html', {'form': form})

# def property_edit(request, pk):
#     tenant = Tenant.objects.get(pk=pk)
#     if request.method == "POST":
#         form = TenantForm(request.POST, instance=tenant)
#         if form.is_valid():
#             tenant = form.save()
#             return redirect('tenant_detail', pk=tenant.pk)
#     else:
#         form = TenantForm(instance=tenant)
#     return render(request, 'Rental_hub/tenant_form.html', {'form': form})

def tenant_list(request):
    tenants = Tenant.objects.all()
    return render(request, 'Rental_hub/tenants_list.html', {'tenants': tenants })

def tenant_detail(request, pk):
    tenant = Tenant.objects.get(id=pk)
    return render(request, 'Rental_hub/tenant_detail.html', {'tenant': tenant})

def tenant_create(request):
    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            tenant = form.save()
            return redirect('tenant_detail', pk=tenant.pk)
    else:
        form = TenantForm()
    return render(request, 'Rental_hub/tenant_form.html', {'form': form})

# def tenant_edit(request, pk):
#     tenant = Tenant.objects.get(pk=pk)
#     if request.method == "POST":
#         form = TenantForm(request.POST, instance=tenant)
#         if form.is_valid():
#             tenant = form.save()
#             return redirect('tenant_detail', pk=tenant.pk)
#     else:
#         form = TenantForm(instance=tenant)
#     return render(request, 'Rental_hub/tenant_form.html', {'form': form})