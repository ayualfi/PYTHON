from abc import ABC, abstractmethod
class BangunLengkung(ABC):
    @abstractmethod
    def set_data(self, radius):
        pass
    @abstractmethod
    def hitung_luas(self):
        pass
    @abstractmethod
    def hitung_volume(self):
        pass
class Lingkaran (BangunLengkung):
    def __init__(self, radius=0):
        self.__radius=radius
    def set_data(self, radius):
        self.__radius=radius
    def get_data(self):
        return self.__radius
    def hitung_luas(self):
        return 3.14*self.__radius**2
    def hitung_volume(self):
        print("Lingkaran tidak memiliki volume")
class Tabung(BangunLengkung):
    def __init__(self, radius=0, height_tabung=0):
        self.__radius=radius
        self.__heightT=height_tabung
    def set_data(self, radius):
        self.__radius=radius
    def get_data(self):
        return self.__radius
    def set_heightT(self, heightT):
        self.__heightT=heightT
    def get_heightT(self):
        return self.__heightT
    def hitung_luas(self):
        return 2*3.14*self.__radius*(self.__radius+self.__heightT)
    def hitung_volume(self):
        return 3.14*self.__radius**2*self.__heightT

def info(Bentuk):
    print("Informasi Bangun Lengkung: ", type(Bentuk).__name__)
    print("Luas: ", Bentuk.get_data())
    print("Luas: ", Bentuk.hitung_luas())
    print("Volume: ", Bentuk.hitung_volume())
    print(".."*30)

koin=Lingkaran(4)
kaleng=Tabung(0)
kaleng.set_data(10)
kaleng.set_heightT(10)
kaleng.get_data()
kaleng.get_heightT()

daftar_bentuk=[koin, kaleng]
for bentuk in daftar_bentuk:
    info(bentuk)


