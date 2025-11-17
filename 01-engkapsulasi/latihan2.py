class mahasiswa:
    def __init__(self, nim=0, nama="nama", nilaiUTS=0, nilaiUAS=0):
        self.__nim=nim
        self.__nama=nama
        self.__nilaiUTS=nilaiUTS
        self.__nilaiUAS=nilaiUAS
    def set_nama(self, nama):
        self.__nama=nama
    def get_nama(self):
        return self.__nama
    def set_nim(self, nim):
        self.__nim=nim
    def get_nim(self):
        return self.__nim
    def set_nilaiUTS(self, nilaiUTS):
        self.__nilaiUTS=nilaiUTS
    def get_nilaiUTS(self):
        return self.__nilaiUTS
    def set_nilaiUAS(self, nilaiUAS):
        self.__nilaiUAS=nilaiUAS
    def get_nilaiUAS(self):
        return self.__nilaiUAS
    def info(self):
        print(f"Nama= \t {self.__nama}")
        print(f"Nim= \t {self.__nim}")
        print(f"UTS= \t {self.__nilaiUTS}")
        print(f"Nama= \t {self.__nilaiUAS}")
        print(f"Rata-rata= \t ", (self.__nilaiUTS+self.__nilaiUAS)/2)
#bismillah jalan
#tanpa get
mahasiswi1=mahasiswa()
mahasiswi1.set_nama("Ayu Alfi Hidayati")
mahasiswi1.set_nim(2421400175)
mahasiswi1.set_nilaiUTS(90)
mahasiswi1.set_nilaiUAS(90)
mahasiswi1.info()

#dengan get
print("NYOBA IMPLEMENTASI GET")
mahasiswi2=mahasiswa()
mahasiswi2.set_nama("Ayu Alfi Hidayati")
mahasiswi2.set_nim(2421400175)
mahasiswi2.set_nilaiUTS(90)
mahasiswi2.set_nilaiUAS(90)
print("Nama= ", mahasiswi2.get_nama())
print("Age= ", mahasiswi2.get_nim())
print("UTS= ", mahasiswi2.get_nilaiUTS())
print("UAS= ", mahasiswi2.get_nilaiUAS())
print("Rata-rata= ", (mahasiswi2.get_nilaiUTS()+mahasiswi2.get_nilaiUAS())/2)




