# Percabangan
# Struktur
"""
    1.if -nya
    2.Punya kondisi
    3.pumya aksi
"""
nama = input ("Masukan nama : ")

#Percabangan ynag inline (satu baris)
if nama == "king restu" : print ("lembo ade lenga")

# Percabangan indentasi
if nama == "kokong":
    print ("apanyani idong")

    # Percabangan 1 kondisi 2 aksi
    # Pakai kata kunci "else"
    
    if nama =="kokong":
        print(f"apanyani idong {nama}")
    else:
        print (f'anda{nama},bukan kokong')
    print ("kenapa pian")