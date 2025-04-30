from django.shortcuts import render, redirect
import re

def odeme_baslat(request):
    if request.method == "POST":
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')

        # Basit geçerlilik kontrolleri
        if (
            re.fullmatch(r"\d{16}", card_number) and  # 16 haneli sayı
            re.fullmatch(r"\d{2}/\d{2}", expiry_date) and  # MM/YY formatı
            re.fullmatch(r"\d{3}", cvv)  # 3 haneli sayı
        ):
            return render(request, 'ödeme_sonuc.html', {
                'card_number': card_number[-4:],  # son 4 hane gösterilir
                'expiry_date': expiry_date
            })
        else:
            return render(request, 'ödeme_hata.html')

    return render(request, 'ödeme.html')
