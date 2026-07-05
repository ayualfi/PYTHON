from django.shortcuts import render

# Create your views here.
def beranda(request):
  return render(request, 'mahasiswa/beranda.html',{
    "page_title":"Dashboard",
    "breadcrumb": "Beranda",
  })
def about(request):
  return render(request, 'mahasiswa/about.html',{
    "page_title":"about",
    "breadcrumb": "about",
  })
def pesanan(request):
  return render(request, 'mahasiswa/pesanan.html',{
    "page_title":"pesanan",
    "breadcrumb": "pesanan",
  })
def pelanggan(request):
  return render(request, 'mahasiswa/pelanggan.html',{
    "page_title":"pelanggan",
    "breadcrumb": "pelanggan",
  })
def produk(request):
  return render(request, 'mahasiswa/produk.html',{
    "page_title":"produk",
    "breadcrumb": "produk",
  })
def keuangan(request):
  return render(request, 'mahasiswa/keuangan.html',{
    "page_title":"keuangan",
    "breadcrumb": "keuangan",
  })
def laporan(request):
  return render(request, 'mahasiswa/laporan.html',{
    "page_title":"laporan",
    "breadcrumb": "laporan",
  })
def pengaturan(request):
  return render(request, 'mahasiswa/pengaturan.html',{
    "page_title":"pengaturan",
    "breadcrumb": "pengaturan",
  })

