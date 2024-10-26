from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def Pendidikan(request):
    return render(request, 'Pendidikan.html')

def PengalamanKerja(request):
    return render(request, 'PengalamanKerja.html')

def Kontak(request):
    return render(request, 'Kontak.html')
