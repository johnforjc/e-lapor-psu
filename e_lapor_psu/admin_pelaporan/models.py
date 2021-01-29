from django.db import models
from pelaporan.models import DataPerusahaan
from pelaporan.models import DataProyek

# Create your models here.

def get_nama_perusahaan(id):

    query = DataPerusahaan.objects.get(id_data_perusahaan_id = id)
    return query.nama_perusahaan

def get_lokasi_proyek(id):
    query = DataProyek.objects.get(id_data_proyek = id)
    return query.lokasi_proyek