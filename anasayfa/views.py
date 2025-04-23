

from django.shortcuts import render, redirect
from .models import Siparis

def home(request):

    return render(request, 'anasayfa.html')

def siparis_ver(request):
    if request.method == 'POST':
        urun = request.POST.get('urun_adi')
        Siparis.objects.create(urun_adi=urun)
        return redirect('order')  # ya da teşekkür sayfası
    return redirect('order')



