class Orang:
    def __init__(self, nama_mu=""):
        self.nama=nama_mu
    def siapa_nama_mu (self):
        print("Nama= ", self.nama)
class Mahasiswa:
    def __init__(self, nim_mu="", jurusan_mu=""):
        self.nim=nim_mu
        self.jurusan=jurusan_mu
    def berapa_nim_mu(self):
        print("NIM= ", self.nim)
    def apa_jurusan_mu(self):
        print("Jurusan= ", self.jurusan)
class Pegawai:
    def __init__(self, nip_mu="", jabatan_mu=""):
        self.nip=nip_mu
        self.jabatan=jabatan_mu
    def berapa_nip_mu(self):
        print("NIP= ", self.nip)
    def apa_jabatan_mu(self):
        print("Jabatan= ", self.jabatan)
class Asisten_Riset(Orang, Mahasiswa, Pegawai):
    def __init__(self, proyek_mu=""):
        self.proyek=proyek_mu
    def apa_proyek_mu(self):
        print("Proyek= ", self.proyek)
    def data_lengkap(self):
        self.siapa_nama_mu()
        self.berapa_nim_mu()
        self.apa_jurusan_mu()
        self.berapa_nip_mu()
        self.apa_jabatan_mu()
        self.apa_proyek_mu()

orang1=Asisten_Riset()
orang1.nama="Ayu Alfi H"
orang1.nim="2421400175"
orang1.jurusan="Informatika"
orang1.nip="00002"
orang1.jabatan="Dosen"
orang1.proyek="Nurul Jadid Santri Reporting"
orang1.data_lengkap()
    