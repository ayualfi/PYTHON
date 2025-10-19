class rekening:
    def __init__(self, saldo=0):
        self.__saldo=saldo
    def set_setoran(self, nominal):
        self.__saldo += nominal
    def get_setoran(self):
        return self.__saldo
    def set_penarikan(self, nominal):
        if self.__saldo>50:
            self.__saldo -= nominal
        else:
            print("Saldo mu akan kurang dari 50 jika ditarik")
    def get_penarikan(self):
        return self.__saldo
    def set_statustransfer(self, tujuan, nominal):
        if self.__saldo - nominal>=50:
            self.__saldo -= nominal
            tujuan.__saldo += nominal
        else:
            print("saldo mu akan kurang dari 50 jika di tarik untuk TF. Jadi saldo tetap")
    def info(self):
        print(f"Saldo= \t {self.__saldo}")

#Bismillah Jalan
rekening1=rekening(saldo=60)
rekening2=rekening(saldo=100)

rekening1.set_setoran(50)
rekening2.set_penarikan(40)

rekening1.set_statustransfer(rekening2, 10)

rekening1.info()
rekening2.info()



