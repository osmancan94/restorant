from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.orderss, name='order'),
]
