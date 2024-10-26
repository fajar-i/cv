from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home, name='home'),
    path ('Pendidikan/', views.Pendidikan, name='Pendidikan'),
    path ('PengalamanKerja/', views.PengalamanKerja, name='PengalamanKerja'),
    path ('Kontak/', views.Kontak, name='Kontak'),
]