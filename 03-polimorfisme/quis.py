print(".."*10)
def Jalankan(x):
    return x.start()
class A:
    def start(self):
        return "A mulai"
class B:
    def start (self):
        return "B mulai"
hasil=[Jalankan(o) for o in (A(), B())]
print(hasil)

print(".."*10)
class T:
    def __init__(self, nama, prioritas):
        self.nama=nama
        self.prioritas=prioritas
lst=[T('A',3),T('B',1),T('C',2)]
lst.sort(key=lambda o:o.prioritas)
print([o.nama for o in lst])

print(".."*10)
class Kucing:
    def suara(self):
        print("Meong")
class Anjing:
    def suara(self):
        print("Guk")
def bicara(hewan):
    hewan.suara()
bicara(Kucing())
bicara(Anjing())

print(".."*10)
class Kendaraan:
    def jalan(self):
        return "bergerak"
class Mobil(Kendaraan):
    def jalan(self):
        return "berkendara"
k=Kendaraan()
m=Mobil()
print(k.jalan(), "|", m.jalan())

print(".."*10)
class Persegi:
    def __init__(self, s):
        self.s=s
    def keliling(self):
        return 4*self.s
class Lingkaran: 
    def __init__(self, r):
        self.r=r
    def keliling(self):
        return 2*3.14*self.r
objs=[Persegi(4), Lingkaran(1)]
total=sum(o.keliling() for o in objs)
print(round(total, 2))

print(".."*10)
class Keranjang:
    def __init__(self, items):
        self.items=items
    def __len__(self):
        return len(self.items)
print(len(Keranjang([1,2,3,4])))

print(".."*10)
class Worker:
    def __call__(self,x):
        return x*2 
w=Worker()
print(w(3))

print(".."*10)
class Persegi:
    def __init__(self, s):
        self.s=s
    def luas (self):
        return self.s*self.s
class Lingkaran:
    def __init__(self, r):
        self.r=r
    def luas(self):
        return 3.14*self.r*self.r
shapes=[Persegi(3), Lingkaran(2)]
total=sum(s.luas() for s in shapes)
print(round(total, 2))

print(".."*10) 
class File:
    def __str__(self):
        return "File" 
class User:
    def __str__(self):
        return "User"
print(str(File()), str(User()))

print(".."*10) 
class Koleksi:
    def __init__(self, items):
        self.items=items
    def __iter__(self):
        return iter(self.items)
for x in Koleksi([1, 2, 3]):
    print(x, end ="")

print(".."*10) 
class NotifWA:
    def kirim(self, msg):
        return f"WA:{msg}"
class NotifEmail:
    def kirim (self, msg):
        return f"Email:{msg}"
def broadcast(nots, msg):
        return [n.kirim(msg) for n in nots]
print(broadcast([NotifWA(), NotifEmail()], "Ok"))

print(".."*10) 
class Uang:
    def __init__(self, rp):
        self.rp=rp
    def __add__(self, other):
        return Uang(self.rp+other.rp)
print((Uang(1000)+Uang(500)).rp)

print(".."*10) 
class Persegi:
    def __init__(self, s):
        self.s=s
    def keliling(self):
        return 4*self.s
class Lingkaran:
    def __init__(self, r):
        self.r=r
    def keliling(self):
        return 2*3.14*self.r
data=[Persegi(2), Persegi(3), Lingkaran(1)]
print([d.keliling() for d in data])