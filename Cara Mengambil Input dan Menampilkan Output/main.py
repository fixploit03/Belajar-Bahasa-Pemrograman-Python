# Catatan Rofi dalam belajar Python
# 
# Cara Mengambil Input dan Menampilkan Output

# Input adalah data yang dimasukkan ke dalam program. Sedangkan output adalah data yang dihasilkan oleh program. Python memiliki fungsi input() untuk mengambil input dan fungsi print() untuk menampilkan output.

# Cara mengambil input di Python
# Untuk mengambil input di Python, kita bisa menggunakan fungsi input(). Fungsi ini akan mengembalikan data yang dimasukkan oleh pengguna.
# 
# Contoh:
nama_lengkap = input("Masukkan nama lengkap Anda: ")

# Cara menampilkan output di Python
# Untuk menampilkan output di Python, kita bisa menggunakan fungsi print(). Fungsi ini akan menampilkan data yang diberikan ke layar.
#
# Contoh:
print("Halo,", nama_lengkap)

# Kita juga bisa menampilkan output dengan menggunakan operator + untuk menggabungkan string.
#
# Contoh:
nama_depan = "Rofi"
nama_belakang = "Afrizal"
print("Nama lengkap saya adalah", nama_depan + " " + nama_belakang)
# Output: Nama lengkap saya adalah Rofi Afrizal

# Kita juga bisa menampilkan output dengan menggunakan operator , untuk memisahkan antar data.
#
# Contoh:
nama_depan = "Rofi"
nama_belakang = "Afrizal"
print("Nama lengkap saya adalah", nama_depan, nama_belakang)
# Output: Nama lengkap saya adalah Rofi Afrizal

# Kita juga bisa menampilkan output dengan menggunakan operator % untuk memformat string.
#
# Contoh:
nama_depan = "Rofi"
nama_belakang = "Afrizal"
print("Nama lengkap saya adalah %s %s" % (nama_depan, nama_belakang))
# Output: Nama lengkap saya adalah Rofi Afrizal

# Kita juga bisa menampilkan output dengan menggunakan f-string.
#
# Contoh:
nama_depan = "Rofi"
nama_belakang = "Afrizal"
print(f"Nama lengkap saya adalah {nama_depan} {nama_belakang}")
# Output: Nama lengkap saya adalah Rofi Afrizal
# Dengan f-string, kita bisa langsung memasukkan variabel ke dalam string dengan menggunakan {nama_variabel}.
