class mahasiswa:
    def __init__(self, nama="", nim=""):
        self.nama=nama
        self.nim=nim
    def nama_mahasiswa(self):
        print("Nama= ", self.nama)
    def nim_mahasiswa(self):
        print("NIM= ", self.nim)
class asisten_dosen:
    def __init__(self, matakuliah="", jamasistensi=""):
        self.mata_kuliah=matakuliah
        self.jam_asistensi=jamasistensi
    def mata_kuliah_anda(self):
        print("Mata Kuliah= ", self.mata_kuliah)
    def jam_asisten_anda(self):
        print("Jam asistensi= ", self.jam_asistensi)
class asisten_praktikum(mahasiswa, asisten_dosen):
    def data_lengkap(self):
        self.nama_mahasiswa()
        self.nim_mahasiswa()
        self.mata_kuliah_anda()
        self.jam_asisten_anda()

mahasiswa1=asisten_praktikum()
mahasiswa1.nama="Ayu Alfi Hidayati"
mahasiswa1.nim="2421400175"
mahasiswa1.mata_kuliah="Pemograman berorientasi objek"
mahasiswa1.jam_asistensi="4 SKS"
mahasiswa1.data_lengkap()
    