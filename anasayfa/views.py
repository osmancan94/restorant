from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Siparis
from .models import Urun 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User


def homee(request):
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

        # sepete ekle
        sepet = request.session.get('cart', [])
        sepet.append(urun)
        request.session['cart'] = sepet
        request.session['sepet_urun_sayisi'] = len(sepet)

        # Kullanıcı giriş yaptıysa, siparişi kaydet
        if request.user.is_authenticated:
            Siparis.objects.create(user=request.user, urun_adi=urun)

    return redirect('homee')



def siparislerim(request):
    if request.user.is_authenticated:
        siparisler = Siparis.objects.filter(user=request.user).order_by('-tarih')
    else:
        siparisler = []

    return render(request, 'siparislerim.html', {
        'siparisler': siparisler
    })

 

  

def sepet(request):
    sepet = request.session.get('cart', [])
    toplam_tutar = 0

    for urun_adi in sepet:
        try:
            urun_obj = Urun.objects.get(isim=urun_adi)
            toplam_tutar += float(urun_obj.fiyat)
        except Urun.DoesNotExist:
            pass  

    return render(request, 'sepet.html', {
        'cart': sepet,
        'toplam_tutar': toplam_tutar,
        'sepet_urun_sayisi': len(sepet)
    })



def urun_sil(request, urun_adi):
    sepet = request.session.get('cart', [])

    
    if urun_adi in sepet:
        sepet.remove(urun_adi)
        request.session['cart'] = sepet
        request.session['sepet_urun_sayisi'] = len(sepet)

    return redirect('cart') 


def sepet_temizle(request):
    request.session['cart'] = []
    request.session['sepet_urun_sayisi'] = 0
    return redirect('cart')



def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def profil(request):
    user = request.user

    if request.method == 'POST':
        # Profil bilgilerini güncelle
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        messages.success(request, "Profil başarıyla güncellendi!")

    return render(request, 'profil.html', {'user': user})

@login_required
def sifre_degistir(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Şifre başarıyla değiştirildi!")
            return redirect('profil')
    else:
         form = PasswordChangeForm(user=request.user)

    return render(request, 'sifre_degistir.html', {'form': form})


def yardim(request):
    return render(request, 'yardim.html')

