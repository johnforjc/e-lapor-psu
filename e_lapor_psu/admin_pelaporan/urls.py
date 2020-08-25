from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('listing_proyek/', views.listing_proyek, name='listing_proyek'),
    path('listing_perusahaan/', views.listing_perusahaan, name='listing_perusahaan'),
    path('listing_perizinan/', views.listing_perizinan, name='listing_perizinan'),
]