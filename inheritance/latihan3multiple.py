class Orang:
    def __init__(self, name=""):
        self.nama=name
    def namamu(self):
        print("Nama= ", self.nama)
class Mahasiswa(Orang):
    def __init__(self, name="", NIM="", prodi=""):
        self.nim=NIM
        self.jurusan=prodi
    def nim_mu(self):
        print("Nim mu= ", self.nim_mu)
    def jurusan_mu(self):
        print("Jurusan= ", self.jurusan)
class Pegawai(Orang, Mahasiswa):
    def __init__(self, name="", NIM="", prodi="", NIP="", jabatan=""):
        self.nip=NIP
        self.jabatan=jabatan
    def nip_mu(self):
        print("NIP= ", self.nip)
    def jabatan_mu(self):
        print("Jabatan= ", self.jabatan)
class Asisten_riset(Mahasiswa, Pegawai):
    def __init__(self, name="", NIM="", prodi="", NIP="", jabatan="", proyek=""):
        self.proyek=proyek
    def proyekmu(self):
        print("Proyek= ", self.proyek)
    def data_lengkap(self):
        self.nama()
        self.nim()
        self.jurusan()
        self.nip()
        self.jabatan()
        self.proyek()

orang1=Asisten_riset()
orang1.nama="Ayu Alfi Hidayati"
orang1.nim="2421400175"
orang1.jurusan="IF"
orang1.nip="2222"
orang1.jabatan="Anak dosen"
orang1.proyek="Nurul Jadid Santri Information"
orang1.data_lengkap()
        
        