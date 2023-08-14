from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'M6Ind2'

urlpatterns = [
    path('landing/', views.landing, name='landing'),
    path('usuarios/', views.clientes, name='usuarios'),
    path('registro/', views.registro, name='registro'),
    path('newsletter/', views.createUsuario, name='register'),
    path("login/", auth_views.LoginView.as_view(template_name = 'M6Ind2/login.html'), name="login"), 
    path("logout/", auth_views.LogoutView.as_view(template_name = 'M6Ind2/logout.html'), name="logout"),   
]