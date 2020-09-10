from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from pelaporan.models import DataProyek
from pelaporan.models import DataPerusahaan
from pelaporan.models import DataPerizinan
from pelaporan.models import RumahTapak
from pelaporan.models import RumahSusun
from pelaporan.models import Notifikasi
from pelaporan.models import JenisPsu
import os

EMAIL_HOST_ADMIN = os.environ.get('EMAIL_HOST_USER')
DEFAULT_MEDIA_PATH = os.getcwd() + '/media'

# Create your views here.
def index(request):
    return render(request, 'admin_pelaporan/index_admin_pelaporan.html')

def generate_username(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username+' '+password)
        return render(request, 'admin_pelaporan/generate_username.html')
        
    else:
        return render(request, 'admin_pelaporan/generate_username.html')

def listing_perusahaan(request):
    all_entries = DataPerusahaan.objects.all()
    return render(request, 'admin_pelaporan/list_perusahaan.html', {'all_entries' : all_entries})

def read_perusahaan(request, id):
    entry = DataPerusahaan.objects.get(id_data_perusahaan = id)
    
    ktpPDF = 0
    aktaPDF = 0   

    if entry.ktp_pemilik.url[-4:].lower() == ".pdf":
        ktpPDF = 1
    if entry.akta_pendirian_badan_usaha.url[-4:].lower() == ".pdf":
        aktaPDF = 1

    return render(request, 'admin_pelaporan/read_perusahaan.html', {'entry' : entry, 'ktpPDF' : ktpPDF, 'aktaPDF' : aktaPDF})

def listing_proyek(request, id):
    query = DataProyek.objects.filter(id_data_perusahaan_id = id)
    all_entries = [] 
    for temp in query.all():
        all_entries.append(temp)
    return render(request, 'admin_pelaporan/list_proyek.html', {'all_entries' : all_entries, 'id_data_perusahaan' : id})

def folder_proyek(request, id):
    entry = DataProyek.objects.get(id_data_proyek = id)
    return render(request, 'admin_pelaporan/folder_proyek.html', {'entry' : entry})

def read_proyek(request, id):
    entry = DataProyek.objects.get(id_data_proyek = id)

    return render(request, 'admin_pelaporan/read_proyek.html', {'entry' : entry})

def read_tipe_rumah(request, id):
    entry = DataProyek.objects.get(id_data_proyek = id)

    if entry.jenis_produk == "Rumah Tapak":
        query = RumahTapak.objects.filter(id_data_proyek_id=id)
        rumahTapaks = []
        for temp in query.all():
            rumahTapaks.append(temp)
        
        if not query:
            entry = DataProyek.objects.get(id_data_proyek = id)
            message = "Rincian rumah tapak yang anda cari kosong atau telah dihapus"
            return render(request, 'admin_pelaporan/error_kosong.html', {'entry': entry, 'message': message})
        else:
            return render(request, 'admin_pelaporan/read_tipe_rumah.html', {'entry' : entry, 'rumahTapaks': rumahTapaks})

    elif entry.jenis_produk == "Rumah Susun":
        query = RumahSusun.objects.filter(id_data_proyek_id=id)
        rumahSusuns = []
        for temp in query.all():
            rumahSusuns.append(temp)

        if not query:
            entry = DataProyek.objects.get(id_data_proyek = id)
            message = "Rincian rumah susun yang anda cari kosong atau telah dihapus"
            return render(request, 'admin_pelaporan/error_kosong.html', {'entry': entry, 'message': message})
        else:
            return render(request, 'admin_pelaporan/read_tipe_rumah.html', {'entry' : entry, 'rumahSusuns': rumahSusuns})

def read_jenis_psu(request, id):
    try:
        entry = JenisPsu.objects.get(id_data_proyek_id = id)
        return render(request, 'admin_pelaporan/read_jenis_psu.html', {'entry' : entry})
    except JenisPsu.DoesNotExist:
        entry = DataProyek.objects.get(id_data_proyek = id)
        message = "Jenis PSU yang anda cari kosong atau telah dihapus"
        return render(request, 'admin_pelaporan/error_kosong.html', {'entry': entry, 'message': message})
    
def read_perizinan(request, id):
    try:
        entry = DataPerizinan.objects.get(id_data_proyek_id = id)
        
        sitePlanPDF = 0
        uklUplPDF = 0
        izinMendirikanPDF = 0
        izinPenggunaanPDF = 0

        if entry.site_plan.url[-4:].lower() == ".pdf":
            sitePlanPDF = 1
        if entry.ukl_upl.url[-4:].lower() == ".pdf":
            uklUplPDF = 1   
        if entry.izin_mendirikan_bangunan.url[-4:].lower() == ".pdf":
            izinMendirikanPDF = 1
        if entry.izin_penggunaan_bangunan.url[-4:].lower() == ".pdf":
            izinPenggunaanPDF = 1

        return render(request, 'admin_pelaporan/read_perizinan.html', {'entry': entry, 'sitePlanPDF': sitePlanPDF, 'uklUplPDF': uklUplPDF, 'izinMendirikanPDF': izinMendirikanPDF, 'izinPenggunaanPDF': izinPenggunaanPDF})
    except DataPerizinan.DoesNotExist:
        entry = DataProyek.objects.get(id_data_proyek = id)
        message = "Data perizinan yang anda cari kosong atau telah dihapus"
        return render(request, 'admin_pelaporan/error_kosong.html', {'entry': entry, 'message': message})

def listing_perizinan(request):
    all_entries = DataPerizinan.objects.all()
    return render(request, 'admin_pelaporan/list_perizinan.html', {'all_entries' : all_entries})

def kirim_notifikasi(request, id):
    entry = DataPerusahaan.objects.get(id_data_perusahaan = id)
    if request.method == 'POST':
        isi_notifikasi = request.POST['notifikasi']
        subject_notifikasi = request.POST['subject']
        send_mail(
            subject = subject_notifikasi,
            message = isi_notifikasi,
            from_email = EMAIL_HOST_ADMIN,
            recipient_list = [entry.email],
        )
        notifikasi = Notifikasi.objects.create(
            isi_notifikasi = isi_notifikasi,
            id_data_perusahaan_id = id,
        )
        return redirect('read_perusahaan', id)
    else:
        return render(request, 'admin_pelaporan/kirim_notifikasi.html', {'entry': entry})

def verifikasi_perusahaan_berhasil(request, id):
    DataPerusahaan.objects.filter(id_data_perusahaan=id).update(verified_admin=True)
    return render(request, 'admin_pelaporan/verifikasi_perusahaan_berhasil.html', {'entry': id})

def verifikasi_data_proyek(request, id):
    DataProyek.objects.filter(id_data_proyek = id).update(verified_admin_data_proyek=True)
    return redirect('/admin_pelaporan/verifikasi_proyek_berhasil/'+str(id))

def verifikasi_data_tipe_rumah(request, id):
    DataProyek.objects.filter(id_data_proyek = id).update(verified_admin_tipe_rumah=True)
    return redirect('/admin_pelaporan/verifikasi_proyek_berhasil/'+str(id))

def verifikasi_data_perizinan(request, id):
    DataProyek.objects.filter(id_data_proyek = id).update(verified_admin_data_perizinan=True)
    return redirect('/admin_pelaporan/verifikasi_proyek_berhasil/'+str(id))

def verifikasi_data_psu(request, id):
    DataProyek.objects.filter(id_data_proyek = id).update(verified_admin_jenis_psu=True)
    return redirect('/admin_pelaporan/verifikasi_proyek_berhasil/'+str(id))

def verifikasi_proyek_berhasil(request, id):
    return render(request, 'admin_pelaporan/verifikasi_proyek_berhasil.html', {'entry': id})

## Delete on database
def delete_data_perusahaan(request, id):
    if request.method == 'POST':
        dataPerusahaan = DataPerusahaan.objects.get(id_data_perusahaan=id)

        ## Delete file
        if(dataPerusahaan.akta_pendirian_badan_usaha):
            path_to_delete = DEFAULT_MEDIA_PATH + '/akta_pendirian_badan_usaha/' + dataPerusahaan.akta_pendirian_badan_usaha
            os.remove(path_to_delete)
        if(dataPerusahaan.foto_pemilik):
            path_to_delete = DEFAULT_MEDIA_PATH + '/foto_pemilik/' + dataPerusahaan.foto_pemilik
            os.remove(path_to_delete)
        if(dataPerusahaan.ktp_pemilik):
            path_to_delete = DEFAULT_MEDIA_PATH + '/ktp_pemilik/' + dataPerusahaan.ktp_pemilik
            os.remove(path_to_delete)
        ## End of delete file

        DataPerusahaan.objects.filter(id_data_perusahaan=id).delete()
        return redirect('listing_perusahaan')

def delete_data_proyek(request, id):
    if request.method == 'POST':
        dataProyek = DataProyek.objects.get(id_data_proyek=id)
        id_data_perusahaan = dataProyek.id_data_perusahaan_id
        dataProyek.delete()
        return redirect('listing_proyek', id_data_perusahaan)

def delete_data_perizinan(request, id):
    if request.method == 'POST':
        dataPerizinan = DataPerizinan.objects.get(id_data_proyek_id=id)

        ## Delete file yang ada START
        if(dataPerizinan.site_plan):
            path_to_delete = DEFAULT_MEDIA_PATH + '/site_plan/' + dataPerizinan.site_plan
            os.remove(path_to_delete)
        if(dataPerizinan.ukl_upl):
            path_to_delete = DEFAULT_MEDIA_PATH + '/ukl_upl/' + dataPerizinan.ukl_upl
            os.remove(path_to_delete)
        if(dataPerizinan.izin_mendirikan_bangunan):
            path_to_delete = DEFAULT_MEDIA_PATH + '/izin_mendirikan_bangunan/' + dataPerizinan.izin_mendirikan_bangunan
            os.remove(path_to_delete)
        if(dataPerizinan.izin_penggunaan_bangunan):
            path_to_delete = DEFAULT_MEDIA_PATH + '/izin_penggunaan_bangunan/' + dataPerizinan.izin_penggunaan_bangunan
            os.remove(path_to_delete)

        ## Delete file yang ada END
        id_data_proyek = dataPerizinan.id_data_proyek_id
        dataPerizinan.delete()
        return redirect('folder_proyek', id_data_proyek)

def delete_jenis_psu(request, id):
    if request.method == 'POST':
        jenisPsu = JenisPsu.objects.get(id_data_proyek_id=id)
        id_data_proyek = jenisPsu.id_data_proyek_id
        jenisPsu.delete()
        return redirect('folder_proyek', id_data_proyek)

def delete_tipe_rumah_tapak(request, id):
    if request.method == 'POST':
        rumahTapak = RumahTapak.objects.get(id_rumah_tapak=id)
        id_data_proyek = rumahTapak.id_data_proyek_id
        rumahTapak.delete()
        return redirect('read_tipe_rumah', id_data_proyek)

def delete_tipe_rumah_susun(request, id):
    if request.method == 'POST':
        rumahSusun = RumahSusun.objects.get(id_rumah_susun=id)
        id_data_proyek = rumahSusun.id_data_proyek_id
        rumahSusun.delete()
        return redirect('read_tipe_rumah', id_data_proyek)