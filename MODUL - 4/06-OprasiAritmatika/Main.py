# Operasi Aritmatika

# Variabel dengan  nilai awal
a=10
b=3

#Operasi penjumlahan (+)
hasil = a + b
print(a,"+",b,"=", hasil)

# Operasi Pengurangan
hasil = a - b
print(a,"-",b,"=", hasil)

# Operasi perkalian
hasil = a * b
print(a,"*",b,"=",hasil)

#Operasi pemangkatan
hasil = a / b
print(a,"/",b,"=",hasil)

# operasi pemangkatan
hasil = a ** b
print(a,"**",b,"=",hasil)

#Operasi flordivision
hasil = a // b
print(a,"//",b,"=",hasil)

#Prioritas Operasi
"""
   1.()
   2.Perkalian,pembagian,dll ->*/**//
   3.Jumlah dan pengurangan
"""
x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x,"**",y,"*",z,"+",x, "/",y,"-",y, "%",z,"//",x,"=", hasil)