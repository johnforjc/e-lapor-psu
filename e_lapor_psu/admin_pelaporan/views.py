from django.shortcuts import render, redirect
from pelaporan.models import DataProyek
from pelaporan.models import DataPerusahaan
from pelaporan.models import DataPerizinan
from pelaporan.models import RumahTapak
from pelaporan.models import RumahSusun

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
    return render(request, 'admin_pelaporan/read_proyek.html', {'entry' : entry})

def read_perusahaan(request, id):
    entry = DataPerusahaan.objects.get(id_data_perusahaan = id)
    return render(request, 'admin_pelaporan/read_perusahaan.html', {'entry' : entry})

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

# read perusahaan
def read_perusahaan(request):
    return render(request, 'admin_pelaporan/read_perusahaan.html')