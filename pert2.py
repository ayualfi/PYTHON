#ini definisi class aja, jadi belum dijalankan
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
mobil_saya.warna='Hijau'
mobil_kamu.warna='merah'
#Cara jalankan 1
mobil_kamu.info()
mobil_saya.info()
print("========")
#Cara jalankan 2
#\t=TETAP' \n=NEW LINE
print('Mobil Saya\n','\twarna\t\t=', mobil_saya.warna, '\n\tKecepatan\t=', mobil_saya.kecepatan, 'km/h')

print('Mobil Kamu\n','\twarna\t\t=', mobil_kamu.warna, '\n\tKecepatan\t=', mobil_saya.kecepatan, 'km/h')