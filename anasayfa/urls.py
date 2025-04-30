from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('anasayfa/', views.homee, name='homee'),         
    path('siparis/', views.siparis_ver, name='siparis_ver'),
    path('cart/', views.sepet, name='cart'),     
    path('cart/sil/<str:urun_adi>/', views.urun_sil, name='urun_sil'), 
    path('cart/temizle/', views.sepet_temizle, name='sepet_temizle'),
    path('siparislerim/', views.siparislerim, name='siparislerim'),
    path('profil/', views.profil, name='profil'),
    path('yardim/', views.yardim, name='yardim'),

    path('profil/sifre-degistir/', views.sifre_degistir, name='sifre_degistir'),


    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),     
]
