#Variabel adalah tempat kita menyimpan suatu nilai yang akan kita panggil nanti nama variabelnya, dan nilainya akan tertampir
x=5
y="Ayu"
print(x)
print(y)

#Variabel tidak perlu untuk diberi termasuk tipe apa dia. Untuk variabel yang sama yang terakhir di set lah yang akan di tampilkan
x=5
x="Ini Ayu"
print(x)

#casting
#Kamu bisa mengcasting suatu nilai untuk menyetting tipe nya
x=str(3)
y=int(3)
z=float(3)
print(x)
print(y)
print(z)

#Untuk mengetahui tipe dari suatu nilai, gunakanlah ini 
# " (type(namavarabel))  "
x=5
y="Ayu"
print(type(x))
print(type(y))

#Single or Double quotes?
y="Ayu"
# is as same as
x='x'
print(y, x)

#Nama dari variabel termasuk case sensitive
A="Ayu"
a="A.fat"
print(A)
print(a)