from django.urls import path
from . import views
# from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.properties_list, name='properties_list'),
    path('tenants/', views.tenant_list, name='tenant_list'),
    path('properties/<int:pk>', views.property_detail, name='property_detail'),
    path('tenants/<int:pk>', views.tenant_detail, name='tenant_detail'),
    path('properties/new', views.property_create, name='property_create'),
    path('tenants/new', views.tenant_create, name='tenant_create'),
    path('tenants/<int:pk>/edit', views.tenant_edit, name='tenant_edit'),
    path('properties/<int:pk>/edit', views.property_edit, name='property_edit'),
    path('tenants/<int:pk>/delete', views.tenant_delete, name='tenant_delete'),
    path('properties/<int:pk>/delete', views.property_delete, name='property_delete')
]