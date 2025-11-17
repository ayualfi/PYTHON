from abc import ABC, abstractmethod
class BangunDatar(ABC):
    @abstractmethod
    def hitung_luas(self):
        pass
    @abstractmethod
    def hitung_keliling(self):
        pass
class Persegi(BangunDatar):
    def __init__(self, sisi_persegi=0):
        self.sisi=sisi_persegi
    def hitung_luas(self):
        return self.sisi * self.sisi
    def hitung_keliling(self):
        return 4*self.sisi
class PersegiPanjang(BangunDatar):
    def __init__(self, panjang_persegi_panjang=0, lebar_persegi_panjang=0):
        self.panjang=panjang_persegi_panjang
        self.lebar=lebar_persegi_panjang
    def hitung_luas(self):
        return self.panjang*self.lebar
    def hitung_keliling(self):
        return 2 * (self.panjang+self.lebar)

def display_info(bangun_datar):
    print("Informasi Bangun Datar: ", type(bangun_datar).__name__)
    print("Luas: ", bangun_datar.hitung_luas())
    print("Keliling: ", bangun_datar.hitung_keliling())
    print("__"*30)

origami=Persegi(4)
buku=Persegi(0)
buku.sisi=10
buku_gambar=PersegiPanjang(12, 5)

daftar_bentuk=[origami, buku, buku_gambar]
for bentuk in daftar_bentuk:
    display_info(bentuk)

  

        