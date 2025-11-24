from abc import ABC, abstractmethod
class Barang(ABC):
    def __init__(self, idBarang="", NamaBarang="", Kategori="", Stok=0, HargaDasar=0.0):
        self.__idBarang=idBarang
        self.__NamaBarang=NamaBarang
        self.__Kategori=Kategori
        self.__Stok=Stok
        self.__HargaDasar=HargaDasar
    def set_idbarang (self, idBarang):
        self.__idBarang=idBarang
    def get_idBarang(self):
        return self.__idBarang
    def set_NamaBarang(self, NamaBarang):
        self.__NamaBarang=NamaBarang
    def get_NamaBarang(self):
        return self.__NamaBarang
    def set_Kategori(self, Kategori):
        self.__Kategori=Kategori
    def get_Kategori(self):
        return self.__Kategori
    def set_stok(self, Stok):
        self.__Stok=Stok
    def get_stok(self):
        return self.__Stok
    def set_HargaDasar(self, HargaDasar):
        self.__HargaDasar=HargaDasar
    def get_HargaDasar(self):
        return self.__HargaDasar
    @abstractmethod
    def HargaJual(self):
        pass
class BarangElektronik(Barang):
    def __init__(self, idBarang="", NamaBarang="", Kategori="", Stok=0, HargaDasar=0.0, Garansi="", DayaListrik=0):
        super().__init__(idBarang, NamaBarang, Kategori, Stok, HargaDasar)
        self.__Garansi=Garansi
        self.__DayaListrik=DayaListrik
    def set_Garansi(self, Garansi):
        self.__Garansi=Garansi
    def get_Garansi(self):
        return self.__Garansi
    def set_DayaListrik(self, DayaListrik):
        self.__DayaListrik=DayaListrik
    def get_DayaListrik(self):
        return self.__DayaListrik
    def HargaJual(self):
        return self.get_HargaDasar()+(0.10 * self.get_HargaDasar())
class Pakaian(Barang):
    def __init__(self, idBarang="", NamaBarang="", Kategori="", Stok=0, HargaDasar=0, Ukuran="", Bahan=""):
        super().__init__(idBarang, NamaBarang, Kategori, Stok, HargaDasar)
        self.__Ukuran=Ukuran
        self.__Bahan=Bahan
    def set_Ukuran(self, Ukuran):
        self.__Ukuran=Ukuran
    def get_Ukuran(self):
        return self.__Ukuran
    def set_Bahan(self, Bahan):
        self.__Bahan=Bahan
    def get_Bahan(self):
        return self.__Bahan
    def HargaJual(self):
        if self.__Ukuran in ("XL","XXL") and self.__Bahan == "Premium":
            return self.get_HargaDasar() + 15000 + (0.05 * self.get_HargaDasar())
        elif self.__Ukuran in ("XL", "XXL") and self.__Bahan != "Premium":
            return self.get_HargaDasar() + 15000
        elif self.__Bahan == "Premium":
            return self.get_HargaDasar() + (0.05 * self.get_HargaDasar())
def info (Barang):
    print("Informasi Barang", type(Barang).__name__)
    print("id Barang: ", Barang.get_idBarang())
    print("Nama Barang: ", Barang.get_NamaBarang())
    print("Kategori: ", Barang.get_Kategori())
    print("Stok: ", Barang.get_stok())
    print("Harga Dasar: ", Barang.get_HargaDasar())
    print("Harga Jual: ", Barang.HargaJual())
    print("___"*18)

#implememtasi
Pembeli1=Pakaian()
Pembeli1.set_idbarang("001")
Pembeli1.set_NamaBarang("Kemeja")
Pembeli1.set_Kategori("Wanita")
Pembeli1.set_stok(1)
Pembeli1.set_HargaDasar(100000)
Pembeli1.set_Ukuran("XL")
Pembeli1.set_Bahan("Premium")

Pembeli2=BarangElektronik()
Pembeli2.set_idbarang("002")
Pembeli2.set_NamaBarang("Handphone")
Pembeli2.set_Kategori("Samsung")
Pembeli2.set_stok(2)
Pembeli2.set_HargaDasar(200000)
Pembeli2.set_Garansi("1 Tahun")
Pembeli2.set_DayaListrik(2)

daftar_pembeli=[Pembeli1, Pembeli2]
for barang in daftar_pembeli:
    info(barang)











        

    