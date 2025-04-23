# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # Kayıt sayfası
    path('registration_success/', views.registration_success, name='registration_success'),  # Kayıt başarı sayfası
    path('login/', views.user_login, name='login'),  # Login sayfası
    
]
