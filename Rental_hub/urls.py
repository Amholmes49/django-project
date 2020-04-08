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
    # path('artists/<int:pk>/edit', views.artist_edit, name='artist_edit'),
    # path('songs/<int:pk>/edit', views.song_edit, name='song_edit'),
    # path('artists/<int:pk>/delete', views.artist_delete, name='artist_delete'),
    # path('songs/<int:pk>/delete', views.song_delete, name='song_delete')
]