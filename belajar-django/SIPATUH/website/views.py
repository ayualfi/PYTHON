from django.shortcuts import render
from .models import Berita

# Create your views here.
def beranda(request):
  berita_list = Berita.objects.all().order_by('-tanggal') #mengambil semua berita dan mengurutkanny aberdasarkan tanggal terbaru

  context = {
    'berita_list' : berita_list
  }
  return render(request, 'website/beranda.html', context)
def berita(request):
  return render(request, 'website/berita.html')
def kontak(request):
  return render(request, 'website/kontak.html')
def tentang(request):
  return render(request, 'website/tentang.html')