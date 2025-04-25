from django.shortcuts import render, redirect

from .models import Urun 

def home(request):
    sepet = request.session.get('cart', [])  
    sepet_urun_sayisi = len(sepet)

    urunler = Urun.objects.all()  

    return render(request, 'anasayfa.html', {  
        'sepet_urun_sayisi': sepet_urun_sayisi,
        'urunler': urunler  
    })

def siparis_ver(request):
    if request.method == 'POST':
        urun = request.POST.get('urun_adi')

        sepet = request.session.get('cart', [])
        sepet.append(urun)
        request.session['cart'] = sepet
        request.session['sepet_urun_sayisi'] = len(sepet)

    return redirect('home')  

def sepet(request):
    sepet = request.session.get('cart', [])
    return render(request, 'sepet.html', {
        'cart': sepet,
        'sepet_urun_sayisi': len(sepet)  
    })


def urun_sil(request, urun_adi):
    sepet = request.session.get('cart', [])

    
    if urun_adi in sepet:
        sepet.remove(urun_adi)
        request.session['cart'] = sepet
        request.session['sepet_urun_sayisi'] = len(sepet)

    return redirect('cart') 
