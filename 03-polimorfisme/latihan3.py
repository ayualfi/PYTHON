from abc import ABC, abstractmethod
class Pembayaran (ABC):
    @abstractmethod
    def bayar(self, jumlah):
        pass
    @abstractmethod
    def info(Self):
        pass
class Cash(Pembayaran):
    def bayar(self, jumlah):
        return "Membayar sebanyak= ", jumlah
    def info(Self):
        return "Menggunakan metode pembayaran cash"
class E_Wallet(Pembayaran):
    def bayar(self, jumlah):
        return "Membayar sebanyak= ", jumlah
    def info(Self):
        return "Menggunakan metode pembayaran E-Wallet"
class Cash(Pembayaran):
    def bayar(self, jumlah):
        return "Membayar sebanyak= ", jumlah
    def info(Self):
        return "Menggunakan metode pembayaran cash"
