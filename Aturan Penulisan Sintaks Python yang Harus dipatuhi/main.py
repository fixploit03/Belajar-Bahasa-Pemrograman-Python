# Catatan Rofi dalam belajar Python
# 
# Aturan Penulisan Sintaks Python yang harus dipatuhi

# 1. Penulisan Statement Python
# Statement adalah sebuah intruksi atau kalimat perintah yang akan dieksekusi oleh komputer.
#
# Contoh:
print("Hello, World!")
print("Belajar Python itu menyenangkan!")
nama_lengkap = "Rofi"

# Penulisan satu statement tidak diakhiri dengan tanda titik koma (;)
# Sedangkan jika ingin menulis beberapa statement dalam satu baris, maka harus dipisahkan dengan tanda titik koma (;)
#
# Contoh:
print("Hello, World!"); print("Belajar Python itu menyenangkan!"); nama_lengkap = "Rofi"

# 2. Penulisan String pada Python
# String adalah tipe data yang berisi kumpulan karakter. String harus diapit oleh tanda kutip, baik kutip satu ('') maupun kutip dua ("").
#
# Contoh:
print('Hello, World!')
print("Belajar Python itu menyenangkan!")
print("Nama lengkap saya adalah Rofi")

# Atau bisa juga menggunakan tanda kutip tiga (''' atau """) untuk string yang panjang.
# 
# Contoh:
print('''Hello, World!''')
print("""Belajar Python itu menyenangkan!""")
print("""Nama lengkap saya adalah Rofi""")

# 3. Penulisan Case pada Python
# Python bersifat case sensitive, artinya huruf besar dan huruf kecil dianggap berbeda. Sehingga, penulisan huruf besar dan huruf kecil harus diperhatikan.
# 
# Contoh:
nama_lengkap = "Rofi"
print(nama_lengkap)
Nama_Lengkap = "Asep"
print(Nama_Lengkap)

# Case Style
# Dalam penulisan Python, terdapat beberapa gaya penulisan yang umum digunakan, yaitu:
#
# - Camel Case: namaVariabel
# - Pascal Case: NamaVariabel
# - Snake Case: nama_variabel
#
# Contoh:
namaLengkap = "Ucuy"
NamaLengkap = "Asep"
nama_lengkap = "Rofi"

# 4. Penulisan Blok Program Python
# Python menggunakan indentasi untuk menandai blok program. Indentasi adalah spasi atau tab yang digunakan untuk menuliskan kode program.
#
# Contoh yang benar:
nama_lengkap = "Rofi"
if nama_lengkap == "Rofi":
    print("Selamat datang, Rofi!")
    
for i in range(10):
    print(i)
    
# Contoh yang salah:
nama_lengkap = "Rofi"
if nama_lengkap == "Rofi":
print("Selamat datang, Rofi!")

for i in range(10):
print(i)

# Ada beberapa blok program yang harus menggunakan indentasi, yaitu:
#
# - if, elif, else
# - for, while
# - def, class
# - except, finally
# - with

# 5. Penulisan Komentar pada Python
# Komentar adalah teks yang tidak akan dieksekusi oleh program. Komentar digunakan untuk memberikan penjelasan pada kode program. 
# Komentar pada Python diawali dengan tanda pagar (#). Komentar bisa ditulis pada baris baru atau pada baris yang sama dengan kode program.
# 
# Contoh:
# Ini adalah komentar
print("Hello, World!") # Ini juga komentar

# Semangat belajar Python!
# Happy coding!
