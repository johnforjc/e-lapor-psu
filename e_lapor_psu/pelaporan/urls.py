from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_lapor_pengembang, name='index_lapor_pengembang'),
    path('form_data_perusahaan/', views.form_data_perusahaan, name='form_data_perusahaan'),
    path('form_data_proyek/', views.form_data_proyek, name='form_data_proyek'),
    path('form_data_perizinan/', views.form_data_perizinan, name='form_data_perizinan'),
]
