class siswa:
    # class variabel
    jumlah_siswa = 0
    # konstruktor
    def __init__(self, nama, kelas, alamat, nilai):
        self.nama = nama
        self.kelas = kelas
        self.alamat = alamat
        self.nilai = nilai
        siswa.jumlah_siswa += 1
    
    #methode
    def tampilkan_jumlah(self):
        print("Jumlah siswa:", siswa.jumlah_siswa)

    def viewSiswa(self):
        print("------------------")
        print("Data Siswa")
        print("Nama :", self.nama)
        print("Kelas :", self.kelas)
        print("Alamat :", self.alamat)
        print("------------------")
    
    def viewNilai(self):
        print("Keterangan")
        print("Nama :", self.nama)
        for nilai in self.nilai:
            print("Nilai :", nilai)
        print("------------------")

    def viewKeterangan(self):
        print("Keterangan")
        print("Nama :", self.nama)
        print("Kelas :", self.kelas)
        rata = sum(self.nilai)/len(self.nilai)
        print("Rata-rata :", rata)
        if rata >= 75:
            keterangan = "Lulus."
        else:
            keterangan = "Tidak lulus."
        print("Keterangan :", keterangan)
        print("------------------")

#instansiasi objek
siswa1 = siswa("Finda", "XII MIPA 1", "Magelang", [89,67,85,471])
siswa2 = siswa("Umi", "XII MIPA 2", "Bantul", [89, 97, 85, 87])

#pemanggilan objek siswa 1
siswa1.viewSiswa()
siswa1.viewNilai()
siswa1.viewKeterangan()


#pemanggilan objek siswa 2
siswa2.viewSiswa()
siswa2.viewNilai()
siswa2.viewKeterangan()

print("Jumlah siswa :", siswa.jumlah_siswa)