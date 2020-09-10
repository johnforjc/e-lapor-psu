from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import make_password
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
                messages.error(request, 'Username already exists')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'Email already exists')
                return redirect('register')
            else:
                hash_password = make_password(password1)
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    password = hash_password
                )
            
            user.save()
            return redirect('/')

        else:
            messages.error(request, "Password doesn't match")
            return redirect('register')
        
    else:
        return render(request, 'accounts/register.html')