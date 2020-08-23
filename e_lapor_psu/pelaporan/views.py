from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import DataPerusahaan
from .models import DataPerizinan
from django.core.files.storage import FileSystemStorage

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

        foto_pemilik = request.FILES['foto_pemilik']
        ktp_pemilik = request.FILES['ktp_pemilik']
        akta = request.FILES['akta_pendirian_badan_usaha_atau_badan_hukum']

        dataPerusahaan = DataPerusahaan.objects.create(
            nama_perusahaan= nama_perusahaan,
            akta_pendirian_badan_usaha = akta,
            nama_pemilik   = nama_pemilik,
            foto_pemilik   = foto_pemilik,
            ktp_pemilik= ktp_pemilik,
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
    if request.method == 'POST' and request.FILES['site_plan'] and request.FILES['ukl_upl'] and request.FILES['izin_mendirikan_bangunan'] and request.FILES['izin_penggunaan_bangunan']:
        site_plan = request.FILES['site_plan']
        ukl_upl = request.FILES['ukl_upl']
        izin_mendirikan_bangunan = request.FILES['izin_mendirikan_bangunan']
        izin_penggunaan_bangunan = request.FILES['izin_penggunaan_bangunan']

        dataPerizinan = DataPerizinan.objects.create(
            site_plan = site_plan,
            ukl_upl = ukl_upl,
            izin_mendirikan_bangunan = izin_mendirikan_bangunan,
            izin_penggunaan_bangunan = izin_penggunaan_bangunan,
        )
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
