from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_lapor_pengembang, name='index_lapor_pengembang'),
    path('form_data_perusahaan/', views.form_data_perusahaan, name='form_data_perusahaan'),
    path('form_data_proyek/', views.form_data_proyek, name='form_data_proyek'),
    path('form_data_perizinan/<int:id>/', views.form_data_perizinan, name='form_data_perizinan'),
    path('tipe_rumah_tapak/<int:id>/', views.tipe_rumah_tapak, name='tipe_rumah_tapak'),
    path('tipe_rumah_susun/<int:id>/', views.tipe_rumah_susun, name='tipe_rumah_susun'),
    path('jenis_psu/<int:id>/', views.jenis_psu, name='jenis_psu'),
    path('detail_perusahaan/', views.detail_perusahaan, name='detail_perusahaan'),
]
