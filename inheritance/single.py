class lingkaran:
    def __init__(self, jarijari):
        self.__jarijari = jarijari
    def set_jarijari(self, jarijari):
        self.__jarijari = jarijari
    def get_jarijari(self):
        return self.__jarijari
    def get_luas(self):
        return 3.14 * (self.__jarijari ** 2)
class tabung(lingkaran):
    def __init__(self, jarijari, tinggi):
        super().__init__(jarijari)
        self.__tinggi=tinggi
    def set_tinggi(self, tinggi):
        self.__tinggi=tinggi
    def get_tinggi(self):
        return self.__tinggi
    def get_volume(self):
        return self.get_luas()*self.__tinggi
#implementasi
x = tabung(7, 10)
print("Jari jari lingkaran= ", x.get_jarijari())
print("Luas Lingkaran= ", x.get_luas())
print("Jari-jari tabung= ", x.get_jarijari())
print("Tinggi tabung= ", x.get_tinggi())
print("Luas alas tabung= ", x.get_luas())
print("Volume tabung= ", x.get_volume())