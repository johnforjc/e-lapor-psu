from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('generate_admin/', views.generate_admin, name="ganerate_admin"),

    path('listing_perusahaan/', views.listing_perusahaan, name='listing_perusahaan'),
    path('read_perusahaan/<int:id>/', views.read_perusahaan, name="read_perusahaan"),
    path('listing_proyek/<int:id>/', views.listing_proyek, name='listing_proyek'),

    path('folder_proyek/<int:id>/', views.folder_proyek, name="folder_proyek"),
    path('read_proyek/<int:id>/', views.read_proyek, name="read_proyek"),
    path('read_tipe_rumah/<int:id>/', views.read_tipe_rumah, name="read_tipe_rumah"),
    path('read_jenis_psu/<int:id>/', views.read_jenis_psu, name="read_jenis_psu"),
    path('read_perizinan/<int:id>/', views.read_perizinan, name="read_perizinan"),
    
    path('listing_perizinan/', views.listing_perizinan, name='listing_perizinan'),
    path('kirim_notifikasi/<int:id>/', views.kirim_notifikasi, name='kirim_notifikasi'),
    path('verifikasi_perusahaan_berhasil/<int:id>/', views.verifikasi_perusahaan_berhasil, name='verifikasi_perusahaan_berhasil'),
    path('verifikasi_proyek_berhasil/<int:id>/', views.verifikasi_proyek_berhasil, name='verifikasi_proyek_berhasil'),
    path('verifikasi_data_proyek/<int:id>', views.verifikasi_data_proyek, name="verifikasi_data_proyek"),
    path('verifikasi_data_tipe_rumah/<int:id>', views.verifikasi_data_tipe_rumah, name="verifikasi_data_tipe_rumah"),
    path('verifikasi_data_perizinan/<int:id>', views.verifikasi_data_perizinan, name="verifikasi_data_perizinan"),
    path('verifikasi_data_psu/<int:id>', views.verifikasi_data_psu, name="verifikasi_data_psu"),

    ## Delete database
    path('delete_data_perusahaan/<int:id>/', views.delete_data_perusahaan, name='delete_data_perusahaan'),
    path('delete_data_proyek/<int:id>/', views.delete_data_proyek, name='delete_data_proyek'),
    path('delete_data_perizinan/<int:id>/', views.delete_data_perizinan, name='delete_data_perizinan'),
    path('delete_jenis_psu/<int:id>/', views.delete_jenis_psu, name='delete_jenis_psu'),
    path('delete_tipe_rumah_tapak/<int:id>/', views.delete_tipe_rumah_tapak, name='delete_tipe_rumah_tapak'),
    path('delete_tipe_rumah_susun/<int:id>/', views.delete_tipe_rumah_susun, name='delete_tipe_rumah_susun'),
]