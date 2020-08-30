from django.shortcuts import render, redirect
from pelaporan.models import DataProyek
from pelaporan.models import DataPerusahaan
from pelaporan.models import DataPerizinan
from pelaporan.models import RumahTapak
from pelaporan.models import RumahSusun
import os

# Create your views here.
def index(request):
    return render(request, 'admin_pelaporan/index_admin_pelaporan.html')

def listing_proyek(request):
    all_entries = DataProyek.objects.all()
    return render(request, 'admin_pelaporan/list_proyek.html', {'all_entries' : all_entries})

def listing_perusahaan(request):
    all_entries = DataPerusahaan.objects.all()
    return render(request, 'admin_pelaporan/list_perusahaan.html', {'all_entries' : all_entries})

def listing_perizinan(request):
    all_entries = DataPerizinan.objects.all()
    return render(request, 'admin_pelaporan/list_perizinan.html', {'all_entries' : all_entries})

def listing_rumah_tapak(request):
    all_entries = RumahTapak.objects.all()
    return render(request, 'admin_pelaporan/listing_rumah_tapak.html', {'all_entries' : all_entries})

def listing_rumah_susun(request):
    all_entries = RumahSusun.objects.all()
    return render(request, 'admin_pelaporan/listing_rumah_susun.html', {'all_entries' : all_entries})

def read_proyek(request, id):
    entry = DataProyek.objects.get(id_data_proyek = id)

    if entry.jenis_produk == "Rumah Tapak":
        query = RumahTapak.objects.filter(id_data_proyek_id=id)
        rumahTapaks = []
        for temp in query.all():
            rumahTapaks.append(temp)
        return render(request, 'admin_pelaporan/read_proyek.html', {'entry' : entry, 'rumahTapaks': rumahTapaks})

    elif entry.jenis_produk == "Rumah Susun":
        query = RumahSusun.objects.filter(id_data_proyek_id=id)
        rumahSusuns = []
        for temp in query.all():
            rumahSusuns.append(temp)

    return render(request, 'admin_pelaporan/read_proyek.html', {'entry' : entry, 'rumahSusuns': rumahSusuns})

def read_perusahaan(request, id):
    entry = DataPerusahaan.objects.get(id_data_perusahaan = id)
    
    ktpPDF = 0
    aktaPDF = 0   

    if entry.ktp_pemilik.url[-4:] == ".pdf":
        ktpPDF = 1
    if entry.akta_pendirian_badan_usaha.url[-4:] == ".pdf":
        aktaPDF = 1

    return render(request, 'admin_pelaporan/read_perusahaan.html', {'entry' : entry, 'ktpPDF' : ktpPDF, 'aktaPDF' : aktaPDF})

def read_perizinan(request, id):
    entry = DataPerizinan.objects.get(id_data_proyek = id)
    return render(request, 'admin_pelaporan/read_perizinan.html', {'entry' : entry})

def generate_username(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username+' '+password)
        return render(request, 'admin_pelaporan/generate_username.html')
        
    else:
        return render(request, 'admin_pelaporan/generate_username.html')