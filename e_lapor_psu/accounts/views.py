from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request, 'USERNAME TELAH TERPAKAI, MOHON MENGGUNAKAN USERNAME LAIN')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'EMAIL TELAH TERPAKAI, MOHON MENGGUNAKAN EMAIL LAIN')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    password = password1
                )
                user.save()
                auth.login(request, user)
                return redirect('/')

        else:
            messages.error(request, "PASSWORD TIDAK SAMA, SILAHAKAN MENGECEK ULANG PASSWORD")
            return redirect('register')
        
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        print(user)

        if user is not None:
            auth.login(request, user)
            if user.is_superuser == 1:
                return redirect('index')
            else:
                return redirect('/')
        else:
            messages.error(request, "PASSWORD SALAH ATAU AKUN TIDAK DITEMUKAN")
            return redirect('login')
        
    else:
        return render(request, 'accounts/login.html')

def logout(request):
        auth.logout(request)
        return redirect("/")