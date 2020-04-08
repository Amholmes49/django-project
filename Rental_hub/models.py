from django.db import models
from phone_field import PhoneField

Property_type_CHOICES= [
    ('Apartment', 'Apartment'),
    ('SFH', 'Single Family Home'),
    ('Duplex/Triplex/Townhouse', 'Duplex/Triplex/Townhouse'),
    ('Mobile/Manufactured', 'Mobile/Manufactured'),
    ('Commercial', 'Commercial'),
    ]

# Create your models here.
class Property(models.Model):
    photo_url = models.TextField()
    name = models.CharField(max_length=100)
    property_type = models.CharField(max_length=30, choices=Property_type_CHOICES, default='SFH') 
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.IntegerField(max_length=6)
    


    def __str__(self):
        return self.name

class Tenant(models.Model):
    property_name = models.ForeignKey(Property, on_delete=models.PROTECT, related_name='tenants')
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = PhoneField(max_length=20)
    lease_start = models.DateField()
    lease_end = models.DateField()
    
    def __str__(self):
        return self.full_name
