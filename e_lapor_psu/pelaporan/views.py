from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import DataPerusahaan
from .models import DataPerizinan
from .models import DataProyek
from .models import RumahTapak
from .models import RumahSusun
from django.core.files.storage import FileSystemStorage
from django.template.defaulttags import register

@register.filter
def get_range(value):
    return range(1,value+1)

# Create your views here.

def index_lapor_pengembang(request):
    return render(request, 'pengembang_pelaporan/index_lapor_pengembang.html')

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
        
        if jenis_produk == "rumah_tapak":
            return redirect('tipe_rumah_tapak', id=dataProyek.id_data_proyek)
        elif jenis_produk == "rumah_susun":
            return redirect('tipe_rumah_susun', id=dataProyek.id_data_proyek)

    else:
        return render(request, 'pengembang_pelaporan/form_data_proyek.html')

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
        return render(request, 'pengembang_pelaporan/form_data_perizinan.html')

def tipe_rumah_tapak(request, id):
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

        # POST data upload here
        return HttpResponse('sukses')

    else:
        dataProyek = DataProyek.objects.get(id_data_proyek=id)
        jumlah_tipe = dataProyek.jumlah_tipe_rumah
        return render(request, 'pengembang_pelaporan/tipe_rumah_tapak.html', {'jumlah_tipe' : jumlah_tipe})

def tipe_rumah_susun(request, id):
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

        # POST data upload here
        return HttpResponse('Hello')

    else:
        dataProyek = DataProyek.objects.get(id_data_proyek=id)
        jumlah_tipe = dataProyek.jumlah_tipe_rumah
        return render(request, 'pengembang_pelaporan/tipe_rumah_susun.html', {'jumlah_tipe' : jumlah_tipe})

def generate_username(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username+' '+password)
        return render(request, 'generate_username.html')
        
    else:
        return render(request, 'generate_username.html')

    
