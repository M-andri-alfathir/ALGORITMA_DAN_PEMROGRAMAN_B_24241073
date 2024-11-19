# Operasi Komperasi

# setiap kali hasil komperasi selalu bertipe boolean (TRUE/FALSE)

# >,<,=,!=,>=,<=,is,dan is not

# deklarasi variabel

a=4
b=2

#Lebih dari (>)
print("===lebih besar dari (>)")
hasil = a > 2 # TRUE
print(a,">",2,"=", hasil)
hasil = b > 3 # FALSE
print(b,">",3,"=", hasil)

#Kurang dari (<)
print("===lebih besar dari (<)")
hasil = a > 2 # FALSE
print(a,"<",2,"=", hasil)
hasil = b > 3 # TRUE
print(b,"<",3,"=", hasil)

#Lebih dari sama dengan(>=)
print("===lebih besar dari (>=)")
hasil = a >= 2 # TRUE
print(a,">=",2,"=", hasil)
hasil = b >= 3 # FALSE
print(b,">=",3,"=", hasil)

#Kurang dari sama dengaan(<=)
print("===lebih besar dari (<=)")
hasil = a <= 2 # FALSE
print(a,"<=",2,"=", hasil)
hasil = b <= 3 # TRUE
print(b,"<=",3,"=", hasil)

#sama dengan (==)
print("==sama dengan (==)")
hasil = a = 2 # FALSE
print(a,"==",2,"=", hasil)
hasil = b = 3 # TRUE
print(b,"==",3,"=", hasil)

#tidak sama dengan (!=)
print("=== tidak sama dengan (!=)")
hasil = a = 2 # TRUE
print(a,"!=",2,"=", hasil)
hasil = b = 3 # FALSE 
print(b,"!=",3,"=", hasil)

# is sebagai komperasi objek
x = 5
y = 5
hasil = x is y
print("nilai x : ",x,"id:", hex(id(x)))
print("nilai y : ",y,"id:", hex(id(y)))
print(x, "is",y,"=",hasil) 