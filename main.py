# SOAL 1 - Menghitung rata-rata
# Tuliskan program untuk Soal 1 di bawah ini
print("NIM\t\t : 0110220045")
print("Nama\t :Evry Nazyli Ciptanto")
print("Program Studi Teknik Informatika\n")

print("SOAL 1 - Menghitung rata-rata")
x = int(input("Masukkan bilangan pertama\t: "))
y = int(input("Masukkan bilangan kedua\t\t: "))
z = int(input("Masukkan bilangan ketiga\t: "))

avg = (x + y + z) / 3
print ('Rata-rata bilangan {0},{1} dan {2} adalah {3}'.format(x,y,z,avg))




# SOAL 2 - Menulis kelipatan bilangan
# Tuliskan program untuk Soal 2 di bawah ini
print("\nSOAL 2 - Menulis Kelipatan bilangan")
a = int(input("Masukkan sebuah bilangan bulat\t : "))
print(a*1,a*2,a*3,a*4,a*5, sep="---", end="")

