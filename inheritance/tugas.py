class pegawai:
    def __init__(self, nama, alamat, gaji):
        self.__Nama=nama
        self.__Alamat=alamat
        self.__GetGaji=gaji
    def set_nama(self, nama):
        self.__Nama=nama
    def get_nama(self):
        return self.__Nama
    def set_alamat(self, alamat):
        self.__Alamat=alamat
    def get_alamat(self):
        return self.__Alamat
    def set_gaji(self, gaji):
        self.__GetGaji = gaji
    def get_gaji(self):
        return self.__GetGaji
class staf(pegawai):
    def __init__(self, nama, alamat, gaji, jmlhkehadiran=0, trfharian=0):
        super().__init__(nama, alamat, gaji)
        self.__jumlahkehadiran=jmlhkehadiran
        self.__tarifharian=trfharian
    def set_jmlhkehadiran(self, jmlhkehadiran):
        self.__jumlahkehadiran=jmlhkehadiran
    def get_jmlhkehadiran(self):
        return self.__jumlahkehadiran
    def set_trfharian(self, trfharian):
        self.__tarifharian=trfharian
    def get_trfharian(self):
        return self.__tarifharian
    def get_gajistaf(self):
        return self.get_gaji() + (self.__jumlahkehadiran*self.__tarifharian)
class dosen(pegawai):
    def __init__(self, nama, alamat, gaji, jmlhsks=0, trfsks=0):
        super().__init__(nama, alamat, gaji)
        self.__jumlahSKS=jmlhsks
        self.__tarifSKS=trfsks
    def set_jmlhsks(self, jmlhsks):
        self.__jumlahSKS=jmlhsks
    def get_jmlhsks(self):
        return self.__jumlahSKS
    def set_trfsks(self, trfsks):
        self.__tarifSKS=trfsks
    def get_trfsks(self):
        return self.__tarifSKS
    def get_gajidosen(self):
        return self.get_gaji() + (self.__jumlahSKS * self.__tarifSKS)

staf1 = staf("Ayu", "Probolinggo",1500000, 4, 50000)
print("Nama staf= ", staf1.get_nama())
print("Alamat= ", staf1.get_alamat())
print("Jumlah Kehadiran= ", staf1.get_jmlhkehadiran())
print("Tarif Harian= ", staf1.get_trfharian())
print("Gaji= ", staf1.get_gajistaf())
print("========================")
dosen1 = dosen("Alfi", "Probolinggo",1500000, 6, 1000000)
print("Nama dosen= ", dosen1.get_nama())
print("Alamat= ", dosen1.get_alamat())
print("Jumlah SKS= ", dosen1.get_jmlhsks())
print("Tarif SKS= ", dosen1.get_trfsks())
print("Gaji= ", dosen1.get_gajidosen())

