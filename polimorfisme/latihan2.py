from abc import ABC, abstractmethod
class BangunLengkung(ABC):
    @abstractmethod
    def hitung_luas(self):
        pass
    @abstractmethod
    def hitung_volume(self):
        pass
class Lingkaran (BangunLengkung):
    def __init__(self, radius_lingkaran=0):
        self.__radiusL=radius_lingkaran
    def set_data(self, radiusL):
        self.__radiusL=radiusL
    def get_data(self):
        return self.__radiusL
    def hitung_luas(self):
        return 3.14*self.__radiusL**2
    def hitung_volume(self):
        print("Lingkaran tidak memiliki volume")
class Tabung(BangunLengkung):
    def __init__(self, radius_tabung=0, height_tabung=0):
        self.__radiusT=radius_tabung
        self.__heightT=height_tabung
    def set_radiusT(self, radiusT):
        self.__radiusT=radiusT
    def get_radiusT(self):
        return self.__radiusT
    def set_heightT(self, heightT):
        self.__heightT=heightT
    def get_heightT(self):
        return self.__heightT
    def hitung_luas(self):
        return 2*3.14*self.__radiusT*(self.__radiusT+self.__heightT)
    def hitung_volume(self):
        return 3.14*self.__radiusT**2*self.__heightT

def info(BangunLengkung):
    print("Informasi Bangun Lengkung: ", type(BangunLengkung).__name__)
    print("Luas: ", BangunLengkung.hitung_luas())
    print("Volume: ", BangunLengkung.hitung_volume())
    print(".."*30)

koin=Lingkaran(4)
kaleng=Tabung(0)
kaleng.set_radiusT(10)
kaleng.set_heightT(10)
kaleng.get_radiusT()
kaleng.get_heightT()

daftar_bentuk=[koin, kaleng]
for bentuk in daftar_bentuk:
    info(bentuk)


