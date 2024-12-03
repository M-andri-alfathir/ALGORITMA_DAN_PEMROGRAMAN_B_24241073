# format string
# kata kunci 'f' '{}'

# contoh umum
# tipe data string

nama = "Isagi Yoichi"
format_string = f"selamat datang {nama}"
print(format_string)
print(f" selamat datang {nama}")

# tipe data boolean
bool = False 
format_str = f"boolean {bool}"
print(format_str)
print(f" selamat datang {nama}")

# angka
angka = 2007.7
format_str = f" angka = {angka}"
print(format_str)

# bilangan bulat
angka = 20
format_str = f" bilangan bulat = {angka :d}"
print(format_str)

# bialngan dengan ordo ribuan
angka = 2000000 # 2,000,000
format_str = f" jutaan = {angka :,}"
print(format_str)

# bilangan desimal
angka = 2008.13253
format_str = f" desimal = {angka :3f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -5
angka_plus = +10,54321
format_minus = f'minus = {angka_minus :-d}'
format_plus = f'plus = {angka_plus :+d}'
print(format_minus)
print(format_plus)

# format persen
persentase = 0.025
format_persentase = f'persentase = {persentase :.2%}'

# melakukan operasi aritmatika
harga = 5000
jumlah = 3

format_string = f'harga total = Rp. {harga*jumlah :,}'
print(format_string)

#