from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import DataPerusahaan

# Create your views here.

def index_lapor_warga(request):
    return render(request, 'index_lapor_pengembang.html')

def form_data_perusahaan(request):
    if request.method == 'POST':
        nama_perusahaan = request.POST['nama_perusahaan']
        nama_pemilik = request.POST['nama_pemilik']
        bentuk_perusahaan = request.POST['bentuk_perusahaan']
        alamat_perusahaan = request.POST['alamat_perusahaan']
        tahun_berdiri = request.POST['tahun_berdiri']
        email = request.POST['email']
        website = request.POST['website']
        nomor_telp = request.POST['no_telp']

        dataPerusahaan = DataPerusahaan.objects.create(
            nama_perusahaan= nama_perusahaan,
            akta_pendirian_badan_usaha = "",
            nama_pemilik   = nama_pemilik,
            foto_pemilik   = "",
            ktp_pemilik= "",
            bentuk_perusahaan  = bentuk_perusahaan,
            alamat_perusahaan  = alamat_perusahaan,
            tahun_berdiri  = tahun_berdiri,
            no_telp= nomor_telp,
            email  = email,
            website= website,
        )

        testing = nama_perusahaan + ' ' + nama_pemilik + ' ' + bentuk_perusahaan + ' ' + alamat_perusahaan + ' ' + tahun_berdiri + ' ' + email + ' ' + website

        # POST data upload here
        return HttpResponse(testing)

    else:
        return render(request, 'form_data_perusahaan.html')

def form_data_perizinan(request):
    if request.method == 'POST':

        # POST data upload here
        return HttpResponse('Hello')

    else:
        return render(request, 'form_data_perizinan.html')

def generate_username(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username+' '+password)
        return render(request, 'generate_username.html')
        
    else:
        return render(request, 'generate_username.html')
