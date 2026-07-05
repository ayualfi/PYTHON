from django.urls import path
from . import views

urlpatterns =[
  path('', views.beranda, name='beranda_page'),
  
  path('about/', views.about, name='about_page'),

  path('pesanan/', views.pesanan, name='pesanan_page'),

  path('pelanggan/', views.pelanggan, name='pelanggan_page'),

  path('produk/', views.produk, name='produk_page'),

  path('keuangan/', views.keuangan, name='keuangan_page'),

  path('laporan/', views.laporan, name='laporan_page'),

  path('pengaturan/', views.pengaturan, name='pengaturan_page'),
]