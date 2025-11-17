from abc import ABC, abstractmethod
class Pembayaran(ABC):
    @abstractmethod
    def validasi(self):
        pass
    @abstractmethod
    def proses(self, jumlah):
        pass
class KartuKredit(Pembayaran):
    def __init__(self, nomor, cvv):
        self.nomor=nomor
        self.cvv=cvv
    def validasi(self):
        if len(self.nomor)==16 and len(self.cvv)==3:
            return True
        else:
            return False
    def proses(self, jumlah):
        if self.validasi():
            return f"Pembayaran sebesar {jumlah} berhasil dengan kartu kredit"
        else:
            return "Validasi kartu kredit gagal"
class EWallet(Pembayaran):
    def __init__(self, No_hp, PIN):
        self.NoHP=No_hp
        self.PIN=PIN
        self.saldo=1000000 #saldo awal EWallet
    def validasi(self):
        return len(self.PIN)==6 #Berarti kalo gak 6 ya gajalan
    def proses(self, jumlah):
        if self.validasi() and self.saldo>=jumlah:
            return f"Pembayaran sebesar {jumlah} berhasil dengan E-Wallet"
        else:
            return "Validasi E-Wallet gagal atau saldo tidak cukup"

#Fungsi untuk melakukan pembayaran
def membayar (metode, jumlah):
    print(metode.proses(jumlah))

#Implementasi
kartu=KartuKredit("1234567812345678", "123")
ewallet=EWallet("123456789", "123456")
membayar(kartu, 500000)
membayar(ewallet, 200000)