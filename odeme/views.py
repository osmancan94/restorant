from django.shortcuts import render, redirect

def odeme_baslat(request):
    if request.method == "POST":
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')

        
        if card_number == "4111111111111111" and expiry_date == "12/23" and cvv == "123":
            
            return render(request, 'ödeme_sonuc.html', {
                'card_number': card_number,
                'expiry_date': expiry_date,
                'cvv': cvv
            })
        else:
            
            return render(request, 'ödeme_hata.html')

    return render(request, 'ödeme.html')
