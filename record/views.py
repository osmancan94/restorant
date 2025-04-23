# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, LoginForm

# Kullanıcı Kayıt View Fonksiyonu
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            login(request, user)
            return redirect('home')  
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})


def registration_success(request):
    return render(request, 'registration_success.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Kullanıcıyı doğrulama
            user = authenticate(request, username=username, password=password)

            if user is not None:  # Kullanıcı doğruysa
                login(request, user)  # Oturum açma
                return redirect('home')  # Ana sayfaya yönlendir
            else:
                form.add_error(None, 'Geçersiz kullanıcı adı veya şifre.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

# Ana Sayfa (Home) View Fonksiyonu
def home(request):
    return render(request, 'home.html')
