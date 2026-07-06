from django.urls import path
from . import views

urlpatterns = [
  path('', views.beranda, name='beranda'),

  path('berita/', views.berita, name='berita'),

  path('kontak/', views.kontak, name='kontak'),

  path('tentang/', views.tentang, name='tentang'),


]