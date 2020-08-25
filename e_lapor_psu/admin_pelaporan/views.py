from django.shortcuts import render, redirect
from pelaporan.models import DataProyek
from pelaporan.models import DataPerusahaan
from pelaporan.models import DataPerizinan

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