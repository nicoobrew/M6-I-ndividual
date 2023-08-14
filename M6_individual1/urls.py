from django.contrib import admin
from django.urls import path, include 
from M6Ind2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('M6Ind2.urls')),
    path('landing/', views.landing),
    path('clientes/', views.clientes)
]
