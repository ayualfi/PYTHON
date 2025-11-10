class Orang:
    def __init__(self, nama_mu=""):
        self.nama=nama_mu
    def siapa_nama_mu(self):
        return self.nama
class Mahasiswa(Orang):
    def __init__(self, nama_mu="", nim_mu=""):
        super().__init__(nama_mu)
        self.nim=nim_mu
    def berapa_nim_mu(self):
        return self.nim
class Asisten(Mahasiswa):
    def __init__(self, nama_mu="", nim_mu="", mata_kuliah_mu=""):
        super().__init__(nama_mu, nim_mu)
        self.mata_kuliah=mata_kuliah_mu
    def apa_mata_kuliah_mu(self):
         return self.mata_kuliah
    def info (self):
        print("Nama= ", self.nama)
        print("NIM= ", self.nim)
        print("Mata Kuliah= ", self.mata_kuliah)

asisten1=Asisten("Ayu Alfi", "2421400175", "Pemograman Berorientasi Objek")
asisten1.info()
