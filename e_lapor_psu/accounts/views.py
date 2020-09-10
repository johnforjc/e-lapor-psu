from django.shortcuts import render

# Create your views here.

# registration
def register(request):
    return render(request, 'accounts/register.html')