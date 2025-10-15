class rekening:
    def __init__(self, saldo=50, setoran=0, penarikan=0, transfer="menambahkan"):
        self.__saldo=saldo
        self.__setoran=setoran
        self.__penarikan=penarikan
        self.__transfer=transfer
    def set_nambahsetoran(self, setoran):
        self.__saldo = self.__saldo+self.__setoran
    def get_nambahsetoran(self):
        return self.__setoran
    def set_nambahpenarikan(self, penarikan):
        self.__saldo = self.__saldo-self.__penarikan
    def get_nambahpenarikan(self):
        return self.__penarikan 
    def set_ayotransfer(self, transfer):
        if self.__transfer=="menambahkan":
            self.__saldo = self.__saldo + self.__transfer
        else:
            self.__saldo = self.__saldo - self.__transfer
    def get_ayotransfer(self):
        return self.__transfer
    def info(self):
        print(f"Saldo= \t {self.__saldo}")
    
#bismillah jalan
#tanpa get
transaksi1=rekening()
transaksi1.set_nambahsetoran(40)
transaksi1.set_nambahpenarikan(20)
transaksi1.set_ayotransfer("menambahkan")
transaksi1.info()
