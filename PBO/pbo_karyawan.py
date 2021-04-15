class karyawan:
    ''' Dasar kelas untuk semua karyawan'''
    jumlah_karyawan = 0

    def __init__(self, nama, gaji, tahun_kelahiran, umur, alamat):
        self.nama = nama
        self.gaji = gaji
        self.tahun_kelahiran = tahun_kelahiran
        self.umur = umur
        self.alamat = alamat
        karyawan.jumlah_karyawan += 1

    def tampilkan_jumlah(self):
        print("Total karyawan:", karyawan.jumlah_karyawan)

    def tampilkan_profil(self):
        print("Nama :", self.nama)
        print("Tahun kelahiran :", self.tahun_kelahiran)
        print("Umur :", self.umur)
    
    def tampilkan_gaji(self):
        print("Nama :", self.nama)
        print("Gaji :", self.gaji)

    def tampilkan_lengkap(self):
        print("Nama :", self.nama)
        print("Alamat :", self.alamat)
        print("Tahun kelahiran :", self.tahun_kelahiran)
        print("Umur :", self.umur)
        print("Gaji :", self.gaji)

# Membuat objek pertama dari kelas karyawan
karyawan1 = karyawan("Chan", 2500000, 1997, 24, "Bantul")

# Membuat objek kedua dari kelas karyawan
karyawan2 = karyawan("Lee know", 2000000, 1998, 23, "Sleman")

# Membuat ojek ketiga dan seterusnya hingga ke delapan
karyawan3 = karyawan("Changbin", 2200000, 1999, 22, "Gunung kidul") 
karyawan4 = karyawan("Hyunjin", 1900000, 2000, 21, "Kota Yogyakarta") 
karyawan5 = karyawan("Han", 2100000, 2000, 21, "Sleman") 
karyawan6 = karyawan("Felix", 1900000, 2000, 21, "Sedayu") 
karyawan7 = karyawan("Seungmin", 1800000, 2000, 21, "Bantul") 
karyawan8 = karyawan("I.N", 1700000, 2001, 20, "Seturan") 

karyawan1.tampilkan_lengkap()
karyawan2.tampilkan_lengkap()
karyawan3.tampilkan_lengkap()
karyawan4.tampilkan_lengkap()
karyawan5.tampilkan_lengkap()
karyawan6.tampilkan_lengkap()
karyawan7.tampilkan_lengkap()
karyawan8.tampilkan_lengkap()

print("Total karyawan :", karyawan.jumlah_karyawan)