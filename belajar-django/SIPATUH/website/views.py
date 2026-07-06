from django.shortcuts import render

# Create your views here.
def beranda(request):
  return render(request, 'website/beranda.html')
def berita(request):
  return render(request, 'website/berita.html')
def kontak(request):
  return render(request, 'website/kontak.html')
def tentang(request):
  return render(request, 'website/tentang.html')