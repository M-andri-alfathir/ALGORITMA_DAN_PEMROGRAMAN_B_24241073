# Input dari pengguna
member = input("Apakah Member? (ya/tidak) : ")
total_belanja = float(input("Masukkan total belanja Rp. "))

# Logika diskon berdasarkan kondisi
if member == "ya":
    if total_belanja > 500000:
        diskon_persen = 20
    else:
        diskon_persen = 10
else:
    if total_belanja >= 500000:
        diskon_persen = 5

# Menghitung diskon dan total yang harus dibayar
diskon = total_belanja * diskon_persen / 100
bayar = total_belanja - diskon

# Output hasil
print(f"\ntotal belanja : Rp. {total_belanja:,.0f}")
print(f"Diskon persen : {diskon_persen}%")
print(f"Diskon Rp. {diskon:,.0f}")
print(f"Bayar Rp. {bayar:,.0f}")