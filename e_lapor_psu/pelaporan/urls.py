from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_lapor_warga, name='index_lapor_warga'),
    path('form_data_perusahaan/', views.form_data_perusahaan, name='form_data_perusahaan')
]
