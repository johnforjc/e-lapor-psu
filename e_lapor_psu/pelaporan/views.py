from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import DataPerusahaan
from .models import DataPerizinan
from .models import DataProyek
from .models import RumahTapak
from .models import RumahSusun
from .models import JenisPsu
from django.core.files.storage import FileSystemStorage
from django.template.defaulttags import register

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
            return redirect('tipe_rumah_tapak', id=dataProyek.id_data_proyek)
        elif jenis_produk == "Rumah Susun":
            return redirect('tipe_rumah_susun', id=dataProyek.id_data_proyek)

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

def jenis_psu(request, id):
    data_proyek = DataProyek.objects.get(id_data_proyek=id)
    if request.method == 'POST':
        jaringan_jalan = request.POST['jaringan_jalan']
        jaringan_saluran_pembuangan_air_hujan = request.POST['jaringan_saluran_pembuangan_air_hujan']
        sanitasi = request.POST['sanitasi']
        jaringan_saluran_pembuangan_air_limbah = request.POST['jaringan_saluran_pembuangan_air_limbah']
        tempat_pembuangan_sampah = request.POST['tempat_pembuangan_sampah']
        sarana_perniagaan = request.POST['sarana_perniagaan']
        sarana_pelayanan_umum_dan_pemerintahan = request.POST['sarana_pelayanan_umum_dan_pemerintahan']
        sarana_pendidikan = request.POST['sarana_pendidikan']
        sarana_kesehatan = request.POST['sarana_kesehatan']
        sarana_peribadatan = request.POST['sarana_peribadatan']
        sarana_rekreasi_dan_olahraga = request.POST['sarana_rekreasi_dan_olahraga']
        sarana_pemakaman = request.POST['sarana_pemakaman']
        sarana_pertanaman_dan_ruang_terbuka_hijau = request.POST['sarana_pertanaman_dan_ruang_terbuka_hijau']
        sarana_parkir = request.POST['sarana_parkir']
        jaringan_air_bersih = request.POST['jaringan_air_bersih']
        jaringan_listrik = request.POST['jaringan_listrik']
        jaringan_telepon = request.POST['jaringan_telepon']
        jaringan_gas = request.POST['jaringan_gas']
        jaringan_transportasi = request.POST['jaringan_transportasi']
        pemadam_kebakaran = request.POST['pemadam_kebakaran']
        sarana_penerangan_jalan_umum = request.POST['sarana_penerangan_jalan_umum']

        jenisPsu = JenisPsu.objects.create(
            jaringan_jalan = jaringan_jalan,
            jaringan_saluran_pembuangan_air_hujan = jaringan_saluran_pembuangan_air_hujan,
            sanitasi = sanitasi,
            jaringan_saluran_pembuangan_air_limbah = jaringan_saluran_pembuangan_air_limbah,
            tempat_pembuangan_sampah = tempat_pembuangan_sampah,
            sarana_perniagaan = sarana_perniagaan,
            sarana_pelayanan_umum_dan_pemerintahan = sarana_pelayanan_umum_dan_pemerintahan,
            sarana_pendidikan = sarana_pendidikan,
            sarana_kesehatan = sarana_kesehatan,
            sarana_peribadatan = sarana_peribadatan,
            sarana_rekreasi_dan_olahraga = sarana_rekreasi_dan_olahraga,
            sarana_pemakaman = sarana_pemakaman,
            sarana_pertanaman_dan_ruang_terbuka_hijau = sarana_pertanaman_dan_ruang_terbuka_hijau,
            sarana_parkir = sarana_parkir,
            jaringan_air_bersih = jaringan_air_bersih,
            jaringan_listrik = jaringan_listrik,
            jaringan_telepon = jaringan_telepon,
            jaringan_gas = jaringan_gas,
            jaringan_transportasi = jaringan_transportasi,
            pemadam_kebakaran = pemadam_kebakaran,
            sarana_penerangan_jalan_umum = sarana_penerangan_jalan_umum,
            id_data_proyek_id = id,
        )

        if JenisPsu:
           DataProyek.objects.filter(id_data_proyek=id).update(verified_jenis_psu = True)

        return redirect('form_data_perizinan', id=id)

    else:
        if data_proyek.verified_jenis_psu == False:
            return render(request, 'pengembang_pelaporan/jenis_psu.html')
        else:
            return redirect('detail_proyek/'+ id +'/')


#### Read on database code

def detail_perusahaan(request, id):
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
    return render(request, 'pengembang_pelaporan/list_proyek.html', {'dataProyeks' : dataProyeks})

def detail_proyek(request, id):
    dataProyek = DataProyek.objects.get(id_data_proyek=id)
    if dataProyek.jenis_produk == "Rumah Tapak":
        query = RumahTapak.objects.filter(id_data_proyek_id=id)
        return render(request, 'pengembang_pelaporan/detail_proyek.html', {'dataProyek' : dataProyek, 'queries': query})
    elif dataProyek.jenis_produk == "Rumah Susun":
        query = RumahSusun.objects.filter(id_data_proyek_id=id)
        return render(request, 'pengembang_pelaporan/detail_proyek.html', {'dataProyek' : dataProyek, 'queries': query})


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
        if request.FILES.get('foto_pemilik', False):
            foto_pemilik = request.FILES['foto_pemilik']
            DataPerusahaan.objects.filter(id_data_perusahaan=id).update(foto_pemilik = foto_pemilik)
        if request.FILES.get('ktp_pemilik', False):
            ktp_pemilik = request.FILES['ktp_pemilik']
            DataPerusahaan.objects.filter(id_data_perusahaan=id).update(ktp_pemilik = ktp_pemilik)
        if request.FILES.get('akta_pendirian_badan_usaha_atau_badan_hukum', False):
            akta = request.FILES['akta_pendirian_badan_usaha_atau_badan_hukum']
            DataPerusahaan.objects.filter(id_data_perusahaan=id).update(akta_pendirian_badan_usaha = akta)

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
            DataPerizinan.objects.filter(id_data_proyek_id=id).update(site_plan = site_plan)
        if request.FILES.get('ukl_upl', False):
            ukl_upl = request.FILES['ukl_upl']
            DataPerizinan.objects.filter(id_data_proyek_id=id).update(ukl_upl = ukl_upl)
        if request.FILES.get('izin_mendirikan_bangunan', False):
            izin_mendirikan_bangunan = request.FILES['izin_mendirikan_bangunan']
            DataPerizinan.objects.filter(id_data_proyek_id=id).update(izin_mendirikan_bangunan = izin_mendirikan_bangunan)
        if request.FILES.get('izin_penggunaan_bangunan', False):
            izin_penggunaan_bangunan = request.FILES['izin_penggunaan_bangunan']
            DataPerizinan.objects.filter(id_data_proyek_id=id).update(izin_penggunaan_bangunan = izin_penggunaan_bangunan)
      
        return redirect('/')

    else:
        return render(request, 'pengembang_pelaporan/update_data_perizinan.html', {'dataPerizinan' : dataPerizinan})

def update_jenis_psu(request, id):
    daftarJenisPsu = JenisPsu.objects.get(id_data_proyek_id=id)
    if request.method == 'POST':
        jaringan_jalan = request.POST['jaringan_jalan']
        jaringan_saluran_pembuangan_air_hujan = request.POST['jaringan_saluran_pembuangan_air_hujan']
        sanitasi = request.POST['sanitasi']
        jaringan_saluran_pembuangan_air_limbah = request.POST['jaringan_saluran_pembuangan_air_limbah']
        tempat_pembuangan_sampah = request.POST['tempat_pembuangan_sampah']
        sarana_perniagaan = request.POST['sarana_perniagaan']
        sarana_pelayanan_umum_dan_pemerintahan = request.POST['sarana_pelayanan_umum_dan_pemerintahan']
        sarana_pendidikan = request.POST['sarana_pendidikan']
        sarana_kesehatan = request.POST['sarana_kesehatan']
        sarana_peribadatan = request.POST['sarana_peribadatan']
        sarana_rekreasi_dan_olahraga = request.POST['sarana_rekreasi_dan_olahraga']
        sarana_pemakaman = request.POST['sarana_pemakaman']
        sarana_pertanaman_dan_ruang_terbuka_hijau = request.POST['sarana_pertanaman_dan_ruang_terbuka_hijau']
        sarana_parkir = request.POST['sarana_parkir']
        jaringan_air_bersih = request.POST['jaringan_air_bersih']
        jaringan_listrik = request.POST['jaringan_listrik']
        jaringan_telepon = request.POST['jaringan_telepon']
        jaringan_gas = request.POST['jaringan_gas']
        jaringan_transportasi = request.POST['jaringan_transportasi']
        pemadam_kebakaran = request.POST['pemadam_kebakaran']
        sarana_penerangan_jalan_umum = request.POST['sarana_penerangan_jalan_umum']

        jenisPsu = JenisPsu.objects.filter(id_data_proyek_id=id).update(
            jaringan_jalan = jaringan_jalan,
            jaringan_saluran_pembuangan_air_hujan = jaringan_saluran_pembuangan_air_hujan,
            sanitasi = sanitasi,
            jaringan_saluran_pembuangan_air_limbah = jaringan_saluran_pembuangan_air_limbah,
            tempat_pembuangan_sampah = tempat_pembuangan_sampah,
            sarana_perniagaan = sarana_perniagaan,
            sarana_pelayanan_umum_dan_pemerintahan = sarana_pelayanan_umum_dan_pemerintahan,
            sarana_pendidikan = sarana_pendidikan,
            sarana_kesehatan = sarana_kesehatan,
            sarana_peribadatan = sarana_peribadatan,
            sarana_rekreasi_dan_olahraga = sarana_rekreasi_dan_olahraga,
            sarana_pemakaman = sarana_pemakaman,
            sarana_pertanaman_dan_ruang_terbuka_hijau = sarana_pertanaman_dan_ruang_terbuka_hijau,
            sarana_parkir = sarana_parkir,
            jaringan_air_bersih = jaringan_air_bersih,
            jaringan_listrik = jaringan_listrik,
            jaringan_telepon = jaringan_telepon,
            jaringan_gas = jaringan_gas,
            jaringan_transportasi = jaringan_transportasi,
            pemadam_kebakaran = pemadam_kebakaran,
            sarana_penerangan_jalan_umum = sarana_penerangan_jalan_umum,
            id_data_proyek_id = id,
        )

        return redirect('form_data_perizinan', id=id)

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

        return redirect("/")
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
    return render(request, 'pengembang_pelaporan/update_tipe_rumah_susun.html', {'RumahTapak' : rumahTapak})
