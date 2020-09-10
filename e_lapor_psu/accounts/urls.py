from django.urls import path
from . import views

urlpatterns=[
    
    ## Registration & Login
    path('register', views.register, name='register')
    
]