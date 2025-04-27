from django.urls import path
from . import views

urlpatterns = [
    path('baslat/',views.odeme_baslat,name='odeme_baslat')
]
