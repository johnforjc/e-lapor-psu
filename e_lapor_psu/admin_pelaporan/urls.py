from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('generate_username/', views.generate_username, name="ganerate_username"),

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
    
]