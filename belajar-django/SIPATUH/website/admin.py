from django.contrib import admin
from .models import Berita

# Register your models here.
@admin.register(Berita)
class BeritaAdmin(admin.ModelAdmin):
    list_display = ('judul', 'tanggal')
    search_fields = ('judul', 'isi')
    list_filter = ('tanggal',)