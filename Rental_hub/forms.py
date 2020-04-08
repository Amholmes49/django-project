from django import forms
from .models import Property, Tenant

class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = ('photo_url', 'name', 'property_type', 'address', 'city', 'state', 'zip')

class TenantForm(forms.ModelForm):

    class Meta:
        model = Tenant
        fields = ('property_name', 'full_name', 'email', 'phone', 'lease_start', 'lease_end')