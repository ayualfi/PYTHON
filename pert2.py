#INI MOBIL SAYA DAN KAMU
#ini definisi class aja, jadi belum dijalankan
from typing import Self


class Mobil:
    '''Kelas untuk merepresentasikan mobil buatan saya'''
    def __init__(self, kecepatan=0, warna='Biru'):
        self.kecepatan=kecepatan
        self.warna=warna
    def injak_gas(self):
        '''Metode untuk menambah kecepatan mobil'''
        self.kecepatan +=5
    def injak_rem(self):
        '''Metode untuk mengurangi kecepatan mobil'''
        self.kecepatan -=3
        if self.kecepatan<0:
            self.kecepatan=0
    def info(self):
        '''Metode untuk menampilkan infomasi kecepatan mobil'''
        print('Warna mobil=', self.warna)
        print('Kecepatan mobil=', self.kecepatan, 'km/jam')

#Ayo jalankan dari sekarang
mobil_saya = Mobil(10)
mobil_kamu = Mobil()
mobil_saya.injak_gas()
mobil_kamu.warna='merah'
#Cara jalankan 1
mobil_kamu.info()
mobil_saya.info()
print("========")
#Cara jalankan 2
#\t=TETAP' \n=NEW LINE
print('Mobil Saya\n','\twarna\t\t=', mobil_saya.warna, '\n\tKecepatan\t=', mobil_saya.kecepatan, 'km/h')

print('Mobil Kamu\n','\twarna\t\t=', mobil_kamu.warna, '\n\tKecepatan\t=', mobil_saya.kecepatan, 'km/h')


print("=============")
#Ini Tentang Lingkaran
class Lingkaran:
    '''Kelas untuk menghitung luas dan keliling lingkaran saya'''
    def __init__(self, jarijari=0):
        self.jarijari=jarijari
        self.luas=0
        self.keliling=0
    '''Metode mengukur luas nya'''
    def hitungluas(self):
        self.luas=self.jarijari**2*3.14
    '''Metode mengukur Kelilingnya'''
    def hitungkeliling(self):
        self.keliling=self.jarijari*2*3.14
    '''Metode untuk menampilkan luas dan keliling lingkaran'''
    def info(self):
        print('Luas Lingkaran= ', self.luas)
        print('keliling Lingkaran= ', self.keliling)

#Ayo jalankan
lingkaran_saya=Lingkaran(7)
lingkaran_saya.hitungkeliling()
lingkaran_saya.hitungluas()
lingkaran_saya.info()

print("=============")
#Ini Tentang AC
class AC:
    '''Kelas untuk menginformasikan status dan suhu AC'''
    def __init__(self, statusAC='mati', suhu=16):
        self.statusAC=statusAC
        self.suhu=suhu
    '''Metode mengetahui status AC'''
    def matikan():
        self.statusAC='mati'
    def hidupkan():
        self.statusAC=='hidup'
    def naikkansuhu(self):
        if statusAC='hidup':
            self.suhu +=1
        else:
            print('AC Mati, hidupkan dulu')
    def turunkansuhu(self):
        if statusAC=='hidup'
            self.suhu -=1
        else:
            print('AC mati, hidupkan dulu')
    def info(self):
        print('Status= ', self.statusAC)
        print('Suhu AC= ', self.suhu)

#Ayo jalan
AC_saya=AC()
AC_saya.hidupkan()
AC_saya.naikkansuhu()
AC_saya.info()
        


