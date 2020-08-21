from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_lapor_warga(request):
    return render(request, 'index_lapor_warga.html')