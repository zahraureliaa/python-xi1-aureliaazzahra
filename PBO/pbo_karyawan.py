class Karyawan:
    ''' Dasar kelas untuk semua karyawan'''
    jumlah_karyawan = 0

    def __init__(self, nama, gaji, umur, alamat):
        self.nama = nama
        self.gaji = gaji
        self.umur = umur
        self.alamat = alamat
        Karyawan.jumlah_karyawan += 1

    def tampilkan_jumlah(self):
        print("Total karyawan:", Karyawan.jumlah_karyawan)

    def tampilkan_profil(self):
        print("Nama :", self.nama)
        print("Umur :", self.umur)
    
    def tampilkan_gaji(self):
        print("Nama :", self.nama)
        print("Gaji :", self.gaji)

    def tampilkan_lengkap(self):
        print("Nama :", self.nama)
        print("Alamat :", self.alamat)
        print("Umur :", self.umur)
        print("Gaji :", self.gaji)

# Membuat objek pertama dari kelas Karyawan
karyawan1 = Karyawan("Sarah", 1000000, 28, "Bantul")

# Membuat objek kedua dari kelas Karyawan
karyawan2 = Karyawan("Budi", 2000000, 31, "Sleman")

# Membuat ojek ketiga
karyawan3 = Karyawan("Fika", 1500000, 26, "Gunung kidul") 

karyawan1.tampilkan_lengkap()
karyawan2.tampilkan_lengkap()
karyawan3.tampilkan_lengkap()
print("Total Karyawan :", Karyawan.jumlah_karyawan)