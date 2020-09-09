from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_lapor_pengembang, name='index_lapor_pengembang'),

    ##  Create on database
    path('form_data_perusahaan/', views.form_data_perusahaan, name='form_data_perusahaan'),
    path('form_data_proyek/', views.form_data_proyek, name='form_data_proyek'),
    path('form_data_perizinan/<int:id>/', views.form_data_perizinan, name='form_data_perizinan'),
    path('tipe_rumah_tapak/<int:id>/', views.tipe_rumah_tapak, name='tipe_rumah_tapak'),
    path('tipe_rumah_susun/<int:id>/', views.tipe_rumah_susun, name='tipe_rumah_susun'),
    path('jenis_psu/<int:id>/', views.jenis_psu, name='jenis_psu'),

    ## Read on database
    path('detail_perusahaan', views.detail_perusahaan, name='detail_perusahaan'),
    path('list_proyek/', views.list_proyek, name='list_proyek'),
    path('folder_proyek/<int:id>/', views.folder_proyek, name="folder_proyek_pengembang"),
    path('detail_proyek/<int:id>/', views.detail_proyek, name='detail_proyek'),
    path('detail_tipe_rumah/<int:id>/', views.detail_tipe_rumah, name="detail_tipe_rumah"),
    path('detail_jenis_psu/<int:id>/', views.detail_jenis_psu, name="detail_jenis_psu"),
    path('detail_perizinan/<int:id>/', views.detail_perizinan, name="detail_perizinan"),

    ## Update database
    path('update_data_perusahaan/<int:id>/', views.update_data_perusahaan, name='update_data_perusahaan'),
    path('update_data_proyek/<int:id>/', views.update_data_proyek, name='update_data_proyek'),
    path('update_data_perizinan/<int:id>/', views.update_data_perizinan, name='update_data_perizinan'),
    path('update_jenis_psu/<int:id>/', views.update_jenis_psu, name='update_jenis_psu'),

    path('update_tipe_rumah_tapak/<int:id>/', views.update_tipe_rumah_tapak, name='update_tipe_rumah_tapak'),
    path('update_tipe_rumah_susun/<int:id>/', views.update_tipe_rumah_susun, name='update_tipe_rumah_susun'),

    path('update_notification', views.update_notification, name='update_notification'),

    ## Error Message
    path('tunggu_verifikasi_perusahaan', views.tunggu_verifikasi_perusahaan, name='tunggu_verifikasi_perusahaan')
]
