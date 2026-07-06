from django.shortcuts import render

# Create your views here.
def beranda(request):
  return render(request, 'mahasiswa/beranda.html',{
    "page_title":"Dashboard",
    "breadcrumb": "Beranda",
  })
def about(request):
  return render(request, 'mahasiswa/about.html',{
    "page_title":"About",
    "breadcrumb": "About",
  })
def pesanan(request):
  return render(request, 'mahasiswa/pesanan.html',{
    "page_title":"Pesanan",
    "breadcrumb": "Pesanan",
  })
def pelanggan(request):
  return render(request, 'mahasiswa/pelanggan.html',{
    "page_title":"Pelanggan",
    "breadcrumb": "Pelanggan",
  })
def produk(request):
  return render(request, 'mahasiswa/produk.html',{
    "page_title":"Produk",
    "breadcrumb": "Produk",
  })
def keuangan(request):
  return render(request, 'mahasiswa/keuangan.html',{
    "page_title":"Keuangan",
    "breadcrumb": "Keuangan",
  })
def laporan(request):
  return render(request, 'mahasiswa/laporan.html',{
    "page_title":"Laporan",
    "breadcrumb": "Laporan",
  })
def pengaturan(request):
  return render(request, 'mahasiswa/pengaturan.html',{
    "page_title":"Pengaturan",
    "breadcrumb": "Pengaturan",
  })

