from django.urls import path
from . import views

urlpatterns = [
    path('anasayfa/', views.home, name='home'),         
    path('siparis/', views.siparis_ver, name='siparis_ver'),
    path('cart/', views.sepet, name='cart'),     
    path('cart/sil/<str:urun_adi>/', views.urun_sil, name='urun_sil'),       
]
