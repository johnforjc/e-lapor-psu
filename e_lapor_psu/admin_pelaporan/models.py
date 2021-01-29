from django.db import models
from pelaporan.models import DataPerusahaan

# Create your models here.

def get_nama_perusahaan(id):

    query = DataPerusahaan.objects.get(id_data_perusahaan_id = id)
    return query.nama_perusahaan