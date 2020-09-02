from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.template.defaulttags import register
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from .models import DataPerusahaan
from .models import DataPerizinan
from .models import DataProyek
from .models import RumahTapak
from .models import RumahSusun
from .models import JenisPsu

@register.filter
def get_range(value):
    return range(1,value+1)

@register.filter
def increment(value):
    value += 1
    return value

# Create your views here.

def index_lapor_pengembang(request):
    return render(request, 'pengembang_pelaporan/index_lapor_pengembang.html')

#### Create on database code

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

        return redirect('/')

    else:
        return render(request, 'pengembang_pelaporan/form_data_perusahaan.html')

def form_data_proyek(request):
    if request.method == 'POST':
        lokasi_proyek = request.POST['lokasi']
        luas_total_area_proyek = request.POST['luas_total_area_proyek']
        jumlah_total_unit = request.POST['jumlah_total_unit_yang_akan_dibangun']
        jenis_produk = request.POST['jenis_produk']
        jumlah_tipe_rumah = request.POST['jumlah_tipe_rumah']
        target_pembangunan = request.POST['target_pembangunan']
        
        id_data_perusahaan = 1
        
        # POST data upload here
        dataProyek = DataProyek.objects.create(
            id_data_perusahaan_id = id_data_perusahaan,
            lokasi_proyek = lokasi_proyek,
            luas_total_area_proyek = luas_total_area_proyek,
            jumlah_total_unit = jumlah_total_unit,
            jenis_produk = jenis_produk,
            jumlah_tipe_rumah = jumlah_tipe_rumah,
            target_pembangunan = target_pembangunan,
        )
        
        if jenis_produk == "Rumah Tapak":
            link = '/tipe_rumah_tapak/'+ str(dataProyek.id_data_proyek)
            return redirect(link)
        elif jenis_produk == "Rumah Susun":
            link = '/tipe_rumah_susun/'+ str(dataProyek.id_data_proyek)
            return redirect(link)

    else:
        return render(request, 'pengembang_pelaporan/form_data_proyek.html')

def form_data_perizinan(request, id):
    data_proyek = DataProyek.objects.get(id_data_proyek=id)
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
            id_data_proyek_id = id,
        )

        if dataPerizinan:
            DataProyek.objects.filter(id_data_proyek=id).update(verified_data_perizinan = True)
        
        return redirect('/')

    else:
        if data_proyek.verified_data_perizinan == False:
            return render(request, 'pengembang_pelaporan/form_data_perizinan.html')
        else:
            return redirect('detail_proyek/'+ id +'/')

def tipe_rumah_tapak(request, id):
    data_proyek = DataProyek.objects.get(id_data_proyek=id)
    if request.method == 'POST':
        jumlah_tipe = int(request.POST['jumlah_tipe'])
        rumahTapak = []

        for iterasi in range(1,jumlah_tipe+1):
            tipe_rumah_tapak = request.POST['tipe_rumah_tapak'+str(iterasi)]
            lb_rumah_tapak = request.POST['lb_rumah_tapak'+str(iterasi)]
            lt_rumah_tapak = request.POST['lt_rumah_tapak'+str(iterasi)]
            jumlah_unit_rumah_tapak = request.POST['jumlah_unit_rumah_tapak'+str(iterasi)]

            rumahTapak.append(
                RumahTapak.objects.create(
                    tipe_rumah_tapak = tipe_rumah_tapak,
                    lb_rumah_tapak = lb_rumah_tapak,
                    lt_rumah_tapak = lt_rumah_tapak,
                    jumlah_unit_rumah_tapak = jumlah_unit_rumah_tapak,
                    id_data_proyek_id = id,
                )
            )
        
        if rumahTapak:
            DataProyek.objects.filter(id_data_proyek=id).update(verified_tipe_rumah = True)

        return redirect('jenis_psu', id=id)

    else:
        if data_proyek.verified_tipe_rumah == False:
            jumlah_tipe = data_proyek.jumlah_tipe_rumah
            return render(request, 'pengembang_pelaporan/tipe_rumah_tapak.html', {'jumlah_tipe' : jumlah_tipe})
        else:
            return redirect('detail_proyek/'+ id +'/')

def tipe_rumah_susun(request, id):
    data_proyek = DataProyek.objects.get(id_data_proyek=id)
    if request.method == 'POST':
        jumlah_tipe = int(request.POST['jumlah_tipe'])
        rumahSusun = []

        for iterasi in range(1,jumlah_tipe+1):
                
            tipe_rumah_susun = request.POST['tipe_rumah_susun'+str(iterasi)]
            lb_rumah_susun = request.POST['lb_rumah_susun'+str(iterasi)]
            jumlah_unit_rumah_susun = request.POST['jumlah_unit_rumah_susun'+str(iterasi)]

            rumahSusun.append(
                RumahSusun.objects.create(
                    tipe_rumah_susun = tipe_rumah_susun,
                    lb_rumah_susun = lb_rumah_susun,
                    jumlah_unit_rumah_susun = jumlah_unit_rumah_susun,
                    id_data_proyek_id = id,
                )
            )

        if rumahSusun:
            DataProyek.objects.filter(id_data_proyek=id).update(verified_tipe_rumah = True)

        return redirect('jenis_psu', id=id)

    else:
        if data_proyek.verified_tipe_rumah == False:
            jumlah_tipe = data_proyek.jumlah_tipe_rumah
            return render(request, 'pengembang_pelaporan/tipe_rumah_susun.html', {'jumlah_tipe' : jumlah_tipe})
        else:
            return redirect('detail_proyek/'+ id +'/')

# Jenis PSU FIX
def jenis_psu(request, id):
    data_proyek = DataProyek.objects.get(id_data_proyek=id)
    if request.method == 'POST':
        my_input = []
        for i in range(1, 22):
            if request.POST.get('inputPSU_'+str(i), False):
                my_input.append(request.POST.get('inputPSU_'+str(i)))
            else:
                my_input.append(0)

        jenisPsu = JenisPsu.objects.create(
            jaringan_jalan = my_input[0],
            jaringan_saluran_pembuangan_air_hujan = my_input[1],
            sanitasi = my_input[2],
            jaringan_saluran_pembuangan_air_limbah = my_input[3],
            tempat_pembuangan_sampah = my_input[4],
            sarana_perniagaan = my_input[5],
            sarana_pelayanan_umum_dan_pemerintahan = my_input[6],
            sarana_pendidikan = my_input[7],
            sarana_kesehatan = my_input[8],
            sarana_peribadatan = my_input[9],
            sarana_rekreasi_dan_olahraga = my_input[10],
            sarana_pemakaman = my_input[11],
            sarana_pertanaman_dan_ruang_terbuka_hijau = my_input[12],
            sarana_parkir = my_input[13],
            jaringan_air_bersih = my_input[14],
            jaringan_listrik = my_input[15],
            jaringan_telepon = my_input[16],
            jaringan_gas = my_input[17],
            jaringan_transportasi = my_input[18],
            pemadam_kebakaran = my_input[19],
            sarana_penerangan_jalan_umum = my_input[20],
            id_data_proyek_id = id,
        )

        if JenisPsu:
           DataProyek.objects.filter(id_data_proyek=id).update(verified_jenis_psu = True)

        return redirect('form_data_perizinan', id=id)

    else:
        if data_proyek.verified_jenis_psu == False:
            return render(request, 'pengembang_pelaporan/jenis_psu.html')
        else:
            return redirect('detail_proyek/'+ str(id) +'/')


#### Read on database code

def detail_perusahaan(request):
    id = 1
    dataPerusahaan = DataPerusahaan.objects.get(id_data_perusahaan=id)
    ktpCheck = 0
    aktaCheck = 0
    if dataPerusahaan.ktp_pemilik.url[-4:] == ".pdf":
        ktpCheck = 1
    if dataPerusahaan.akta_pendirian_badan_usaha.url[-4:] == ".pdf":
        aktaCheck = 1
    return render(request, 'pengembang_pelaporan/detail_perusahaan.html', {'dataPerusahaan' : dataPerusahaan, 'ktpCheck' : ktpCheck, 'aktaCheck' : aktaCheck})

def list_proyek(request):
    id = 1
    query = DataProyek.objects.filter(id_data_perusahaan_id=id)
    dataProyeks = []
    for temp in query.all():
        dataProyeks.append(temp)
    return render(request, 'pengembang_pelaporan/list_proyek.html', {'dataProyeks' : dataProyeks, 'id_data_perusahaan' : id})

def folder_proyek(request, id):
    entry = DataProyek.objects.get(id_data_proyek = id)
    return render(request, 'pengembang_pelaporan/folder_proyek.html', {'entry' : entry})

def detail_proyek(request, id):
    dataProyek = DataProyek.objects.get(id_data_proyek=id)
    return render(request, 'pengembang_pelaporan/detail_proyek.html', {'dataProyek' : dataProyek})

def detail_tipe_rumah(request, id):
    dataProyek = DataProyek.objects.get(id_data_proyek=id)
    if dataProyek.jenis_produk == "Rumah Tapak":
        query = RumahTapak.objects.filter(id_data_proyek_id=id)
        return render(request, 'pengembang_pelaporan/detail_tipe_rumah.html', {'dataProyek' : dataProyek, 'queries': query})
    elif dataProyek.jenis_produk == "Rumah Susun":
        query = RumahSusun.objects.filter(id_data_proyek_id=id)
        return render(request, 'pengembang_pelaporan/detail_tipe_rumah.html', {'dataProyek' : dataProyek, 'queries': query})

def detail_jenis_psu(request, id):
    entry = DataProyek.objects.get(id_data_proyek = id)
    return render(request, 'pengembang_pelaporan/detail_jenis_psu.html', {'entry' : entry})

def detail_perizinan(request, id):
    entry = DataPerizinan.objects.get(id_data_proyek = id)
    return render(request, 'pengembang_pelaporan/detail_perizinan.html', {'entry' : entry})


#### Update on database code

## update data perusahaan FIX
def update_data_perusahaan(request, id):
    dataPerusahaan = DataPerusahaan.objects.get(id_data_perusahaan=id)
    if request.method == 'POST':
        nama_perusahaan = request.POST['nama_perusahaan']
        nama_pemilik = request.POST['nama_pemilik']
        bentuk_perusahaan = request.POST['bentuk_perusahaan']
        alamat_perusahaan = request.POST['alamat_perusahaan']
        tahun_berdiri = request.POST['tahun_berdiri']
        email = request.POST['email']
        website = request.POST['website']
        nomor_telp = request.POST['no_telp']

        dataPerusahaan = DataPerusahaan.objects.filter(id_data_perusahaan=id).update(
            nama_perusahaan= nama_perusahaan,
            nama_pemilik   = nama_pemilik,
            bentuk_perusahaan  = bentuk_perusahaan,
            alamat_perusahaan  = alamat_perusahaan,
            tahun_berdiri  = tahun_berdiri,
            no_telp= nomor_telp,
            email  = email,
            website= website,
        )

        ## Check apakah ada file yang diupdate
        dataPerusahaan = DataPerusahaan.objects.get(id_data_perusahaan=id)
        if request.FILES.get('foto_pemilik', False):
            foto_pemilik = request.FILES['foto_pemilik']
            default_storage.delete(dataPerusahaan.foto_pemilik.path)
            dataPerusahaan.foto_pemilik.name = "foto_pemilik/" + foto_pemilik.name
            new_path = settings.MEDIA_ROOT + "/" + dataPerusahaan.foto_pemilik.name
            path = default_storage.save(new_path, foto_pemilik)
        if request.FILES.get('ktp_pemilik', False):
            ktp_pemilik = request.FILES['ktp_pemilik']
            default_storage.delete(dataPerusahaan.ktp_pemilik.path)
            dataPerusahaan.ktp_pemilik.name = "ktp_pemilik/" + ktp_pemilik.name
            new_path = settings.MEDIA_ROOT + "/" + dataPerusahaan.ktp_pemilik.name
            path = default_storage.save(new_path, ktp_pemilik)
        if request.FILES.get('akta_pendirian_badan_usaha_atau_badan_hukum', False):
            akta = request.FILES['akta_pendirian_badan_usaha_atau_badan_hukum']
            default_storage.delete(dataPerusahaan.akta_pendirian_badan_usaha.path)
            dataPerusahaan.akta_pendirian_badan_usaha.name = "akta_pendirian_badan_usaha/" + akta.name
            new_path = settings.MEDIA_ROOT + "/" + dataPerusahaan.akta_pendirian_badan_usaha.name
            path = default_storage.save(new_path, akta)
        dataPerusahaan.save()

        return redirect('/')

    else:
        return render(request, 'pengembang_pelaporan/update_data_perusahaan.html', {'dataPerusahaan':dataPerusahaan})

## update data proyek FIX
def update_data_proyek(request, id):
    dataProyek = DataProyek.objects.get(id_data_proyek=id)
    if request.method == 'POST':
        lokasi_proyek = request.POST['lokasi']
        luas_total_area_proyek = request.POST['luas_total_area_proyek']
        jumlah_total_unit = request.POST['jumlah_total_unit_yang_akan_dibangun']
        jenis_produk = request.POST['jenis_produk']
        jumlah_tipe_rumah = request.POST['jumlah_tipe_rumah']
        target_pembangunan = request.POST['target_pembangunan']
        
        # kalau sudah ada perusahaan idnya
        id_data_perusahaan = request.POST['id_data_perusahaan']
        
        # POST data upload here
        dataProyek = DataProyek.objects.filter(id_data_proyek=id).update(
            id_data_perusahaan_id = id_data_perusahaan,
            lokasi_proyek = lokasi_proyek,
            luas_total_area_proyek = luas_total_area_proyek,
            jumlah_total_unit = jumlah_total_unit,
            jenis_produk = jenis_produk,
            jumlah_tipe_rumah = jumlah_tipe_rumah,
            target_pembangunan = target_pembangunan,
        )
        redirect_link = "/detail_proyek/" + str(id)
        return redirect(redirect_link)

    else:
        return render(request, 'pengembang_pelaporan/update_data_proyek.html', {'dataProyek': dataProyek})

# update data perizinan FIX
def update_data_perizinan(request, id):
    dataPerizinan = DataPerizinan.objects.get(id_data_proyek_id=id)
    if request.method == 'POST':

        ## Check file ada yang diupload atau tidak
        if request.FILES.get('site_plan', False):
            site_plan = request.FILES['site_plan']
            default_storage.delete(dataPerizinan.site_plan.path)
            dataPerizinan.site_plan.name = "site_plan/" + site_plan.name
            new_path = settings.MEDIA_ROOT + "/" + dataPerizinan.site_plan.name
            path = default_storage.save(new_path, site_plan)
        if request.FILES.get('ukl_upl', False):
            ukl_upl = request.FILES['ukl_upl']
            default_storage.delete(dataPerizinan.ukl_upl.path)
            dataPerizinan.ukl_upl.name = "ukl_upl/" + ukl_upl.name
            new_path = settings.MEDIA_ROOT + "/" + dataPerizinan.ukl_upl.name
            path = default_storage.save(new_path, ukl_upl)
        if request.FILES.get('izin_mendirikan_bangunan', False):
            izin_mendirikan_bangunan = request.FILES['izin_mendirikan_bangunan']
            default_storage.delete(dataPerizinan.izin_mendirikan_bangunan.path)
            dataPerizinan.izin_mendirikan_bangunan.name = "izin_mendirikan_bangunan/" + izin_mendirikan_bangunan.name
            new_path = settings.MEDIA_ROOT + "/" + dataPerizinan.izin_mendirikan_bangunan.name
            path = default_storage.save(new_path, izin_mendirikan_bangunan)
        if request.FILES.get('izin_penggunaan_bangunan', False):
            izin_penggunaan_bangunan = request.FILES['izin_penggunaan_bangunan']
            default_storage.delete(dataPerizinan.izin_penggunaan_bangunan.path)
            dataPerizinan.izin_penggunaan_bangunan.name = "izin_penggunaan_bangunan/" + izin_penggunaan_bangunan.name
            new_path = settings.MEDIA_ROOT + "/" + dataPerizinan.izin_penggunaan_bangunan.name
            path = default_storage.save(new_path, izin_penggunaan_bangunan)
        dataPerizinan.save()
      
        return redirect('/')

    else:
        return render(request, 'pengembang_pelaporan/update_data_perizinan.html', {'dataPerizinan' : dataPerizinan})

def update_jenis_psu(request, id):
    daftarJenisPsu = JenisPsu.objects.get(id_data_proyek=id)
    if request.method == 'POST':
        my_input = []
        for i in range(1, 22):
            if request.POST.get('inputPSU_'+str(i), False):
                my_input.append(request.POST.get('inputPSU_'+str(i)))
            else:
                my_input.append(0)

        jenisPsu = JenisPsu.objects.filter(id_data_proyek=id).update(
            jaringan_jalan = my_input[0],
            jaringan_saluran_pembuangan_air_hujan = my_input[1],
            sanitasi = my_input[2],
            jaringan_saluran_pembuangan_air_limbah = my_input[3],
            tempat_pembuangan_sampah = my_input[4],
            sarana_perniagaan = my_input[5],
            sarana_pelayanan_umum_dan_pemerintahan = my_input[6],
            sarana_pendidikan = my_input[7],
            sarana_kesehatan = my_input[8],
            sarana_peribadatan = my_input[9],
            sarana_rekreasi_dan_olahraga = my_input[10],
            sarana_pemakaman = my_input[11],
            sarana_pertanaman_dan_ruang_terbuka_hijau = my_input[12],
            sarana_parkir = my_input[13],
            jaringan_air_bersih = my_input[14],
            jaringan_listrik = my_input[15],
            jaringan_telepon = my_input[16],
            jaringan_gas = my_input[17],
            jaringan_transportasi = my_input[18],
            pemadam_kebakaran = my_input[19],
            sarana_penerangan_jalan_umum = my_input[20],
            id_data_proyek_id = id,
        )

        return redirect('/detail_proyek/'+ str(id))

    else:
        return render(request, 'pengembang_pelaporan/update_jenis_psu.html', {'daftarJenisPsu': daftarJenisPsu})


## update data rumah susun FIX
def update_tipe_rumah_susun(request, id):
    rumahSusun = RumahSusun.objects.get(id_rumah_susun=id)
    if request.method=='POST':
        tipe_rumah_susun = request.POST['tipe_rumah_susun']
        lb_rumah_susun = request.POST['luas_bangunan']
        jumlah_unit_rumah_susun = request.POST['jumlah_unit']
        id_data_proyek = request.POST["id_proyek"]
        
        rumahSusun = RumahSusun.objects.filter(id_rumah_susun=id).update(
            tipe_rumah_susun = tipe_rumah_susun,
            lb_rumah_susun = lb_rumah_susun,
            jumlah_unit_rumah_susun = jumlah_unit_rumah_susun,
            id_data_proyek_id = id_data_proyek,
        )

        return redirect('/detail_tipe_rumah/' + id_data_proyek)
    else:
        return render(request, 'pengembang_pelaporan/update_tipe_rumah_susun.html', {'RumahSusun' : rumahSusun})


## update data rumah tapak FIX
def update_tipe_rumah_tapak(request, id):
    rumahTapak = RumahTapak.objects.get(id_rumah_tapak=id)
    if request.method=='POST':
        tipe_rumah_tapak = request.POST['tipe_rumah_tapak']
        lb_rumah_tapak = request.POST['lb_rumah_tapak']
        lt_rumah_tapak = request.POST['lt_rumah_tapak']
        jumlah_unit_rumah_tapak = request.POST['jumlah_unit_rumah_tapak']
        id_data_proyek = request.POST["id_proyek"]

        rumahTapak = RumahTapak.objects.filter(id_rumah_tapak=id).update(
            tipe_rumah_tapak = tipe_rumah_tapak,
            lb_rumah_tapak = lb_rumah_tapak,
            lt_rumah_tapak = lt_rumah_tapak,
            jumlah_unit_rumah_tapak = jumlah_unit_rumah_tapak,
            id_data_proyek_id = id_data_proyek,
        )
        return redirect('/detail_tipe_rumah/' + id_data_proyek)
    
    else:
        return render(request, 'pengembang_pelaporan/update_tipe_rumah_tapak.html', {'RumahTapak' : rumahTapak})