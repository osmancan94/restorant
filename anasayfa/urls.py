from django.urls import path
from . import views

urlpatterns = [
    path('anasayfa',views.home,name='home'),
    path('siparis/', views.siparis_ver, name='siparis_ver'),
]
