from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('listing_proyek/', views.listing_proyek, name='listing_proyek'),
    path('listing_perusahaan/', views.listing_perusahaan, name='listing_perusahaan'),
    path('listing_perizinan/', views.listing_perizinan, name='listing_perizinan'),
    path('listing_rumah_tapak/', views.listing_rumah_tapak, name='listing_rumah_tapak'),
    path('listing_rumah_susun/', views.listing_rumah_susun, name='listing_rumah_susun'),
    path('generate_username/', views.generate_username, name="ganerate_username"),
    path('read_proyek/<int:id>/', views.read_proyek, name="read_proyek"),
    path('read_perusahaan/<int:id>/', views.read_perusahaan, name="read_perusahaan"),
    path('read_perizinan/<int:id>/', views.read_perizinan, name="read_perizinan"),

    # testing
    path('read_perusahaan/', views.read_perusahaan, name="read_perusahaan"),
]