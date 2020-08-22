from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_lapor_warga(request):
    return render(request, 'index_lapor_pengembang.html')

def form_data_perusahaan(request):
    return render(request, 'form_data_perusahaan.html')

def isi_data_perusahaan(request):
    return HttpResponse('Success')

def generate_username(request):
    return render(request, 'generate_username.html')