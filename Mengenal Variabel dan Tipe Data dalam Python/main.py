# Catatan Rofi dalam belajar Python
# 
# Mengenal Variabel dan Tipe Data dalam Python

# Pengertian variabel dan tipe data
# Variabel merupakan tempat menyimpan data, sedangkan tipe data adalah jenis data yang tersimpan dalam variabel.

# Membuat Variabel di Python
# Variabel di Python dapat dibuat dengan format seperti ini:
nama_variabel = "nilai variabel"

# Contoh:
nama_lengkap = "Rofi"
umur = 20

# Kemuadian, kita bisa menampilkan variabel dengan menggunakan fungsi print().
#
# Contoh:
print(nama_lengkap)
print(umur)

# Aturan Penulisan Variabel di Python
# - Nama variabel tidak boleh diawali dengan angka.
# - Nama variabel tidak boleh mengandung spasi, gunakan underscore (_) sebagai pengganti spasi.
# - Nama variabel bersifat case sensitive.
# - Nama variabel sebaiknya menggunakan huruf kecil semua.
# - Nama variabel sebaiknya singkat namun deskriptif.
# - Nama variabel sebaiknya tidak menggunakan karakter khusus seperti !, @, #, $, %, dll.

# Mengahpus Variabel di Python
# Untuk menghapus variabel di Python, kita bisa menggunakan fungsi del.
#
# Contoh:
nama_lengkap = "Rofi"
print(nama_lengkap) # Output: Rofi
del nama_lengkap
print(nama_lengkap) # Akan menghasilkan error karena variabel sudah dihapus

# Tipe Data di Python
# Python memiliki beberapa tipe data, diantaranya:
# - String: tipe data yang berisi kumpulan karakter.
# - Integer: tipe data yang berisi bilangan bulat.
# - Float: tipe data yang berisi bilangan desimal.
# - Boolean: tipe data yang berisi nilai
# - List: tipe data yang berisi kumpulan data yang berurutan.
# - Tuple: tipe data yang berisi kumpulan data yang tidak bisa diubah.
# - Set: tipe data yang berisi kumpulan data yang tidak berurutan.
# - Dictionary: tipe data yang berisi kumpulan data dengan format key-value.

# Mengenal Tipe Data String
# String adalah tipe data yang berisi kumpulan karakter. String harus diapit oleh tanda kutip, baik kutip satu ('') maupun kutip dua ("").
#
# Contoh:
nama = "Rofi"
print(nama)

# Atau bisa juga menggunakan tanda kutip tiga (''' atau """) untuk string yang panjang.
#
# Contoh:
nama = '''Rofi'''
print(nama)

# Mengenal Tipe Data Integer
# Integer adalah tipe data yang berisi bilangan bulat.
#
# Contoh:
umur = 20
print(umur)

# Mengenal Tipe Data Float
# Float adalah tipe data yang berisi bilangan desimal.
#
# Contoh:
tinggi_badan = 170.5
print(tinggi_badan)

# Mengenal Tipe Data Boolean
# Boolean adalah tipe data yang berisi nilai True atau False.
#
# Contoh:
benar = True
salah = False
print(benar)
print(salah)

# Mengenal Tipe Data List
# List adalah tipe data yang berisi kumpulan data yang berurutan. List bisa berisi data dengan tipe yang berbeda.
#
# Contoh:
daftar_angka = [1, 2, 3, 4, 5]
daftar_nama = ["Rofi", "Asep", "Ucuy"]
campuran = [1, "Rofi", 2.5, True]
print(daftar_angka)
print(daftar_nama)
print(campuran)

# Mengenal Tipe Data Tuple
# Tuple adalah tipe data yang berisi kumpulan data yang tidak bisa diubah. Tuple bisa berisi data dengan tipe yang berbeda.
#
# Contoh:
tuple_angka = (1, 2, 3, 4, 5)
tuple_nama = ("Rofi", "Asep", "Ucuy")
campuran = (1, "Rofi", 2.5, True)
print(tuple_angka)
print(tuple_nama)
print(campuran)

# Mengenal Tipe Data Set
# Set adalah tipe data yang berisi kumpulan data yang tidak berurutan. Set tidak bisa berisi data yang duplikat.
#
# Contoh:
set_angka = {1, 2, 3, 4, 5}
set_nama = {"Rofi", "Asep", "Ucuy"}
print(set_angka)
print(set_nama)

# Mengenal Tipe Data Dictionary
# Dictionary adalah tipe data yang berisi kumpulan data dengan format key-value. Dictionary tidak bisa berisi data dengan index.
#
# Contoh:
data = {
    "nama": "Rofi",
    "umur": 20,
    "tinggi_badan": 170.5
}
print(data)

# Konversi Tipe Data
# Python mendukung konversi tipe data, yaitu mengubah tipe data satu ke tipe data lain.
#
# Contoh:
umur = 20
umur_str = str(umur)
print(umur_str)

tinggi_badan = 170.5
tinggi_badan_int = int(tinggi_badan)
print(tinggi_badan_int)

# Output:
# 20
# 170

# Semangat belajar Python!
# Happy coding!