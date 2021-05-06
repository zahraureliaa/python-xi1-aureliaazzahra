# INHERITANCE / PEWARISAN
# super class / parent class

class Manusia:
    # konstruktor
    def __init__(self, nama, jk, usia):
        self.nama = nama
        self.jk = jk
        self.usia = usia
    
    def info(self):
        print("Nama: {}\nJenis Kelamin : {}\nUsia : {}".format(self.nama, self.jk, self.usia))
        print("---------------------------")

    def makan(self):
        print("Sedang makan nasi")
        print("----------------------------")

# sub class / child class
class Pelajar(Manusia):
    # konstruktor anak
    def __init__(self, nama, jk, usia, nis, nilai):
        Manusia.__init__(self, nama, jk, usia)
        self.nis = nis
        self.nilai = nilai

    def belajar(self):
        print("{} Sedang belajar". format(self.nama))
        print("------------------------------")
    
    # methode overriding
    def makan(self):
        print("{} sedang sarapan pagi dengan nasi". format(self.nama))
        print("------------------------------")

# sub class / child class
class Pekerja(Manusia):
     # konstruktor anak
    def __init__(self, nama, jk, usia, nip, gaji):
        Manusia.__init__(self, nama, jk, usia)
        self.nip = nip
        self.gaji = gaji

    def bekerja(self):
        print("{} Sedang bekerja". format(self.nama))
        print("------------------------------")

# instansiasi objek
Sam = Pelajar ("Samuel", "Laki-laki", 16, "15234", 90)
Chris = Pekerja("Christopher", "Laki-laki", 29, "1987463", 50000000)

# pemanggilan
# memanggil metode anak
Sam.info()
Sam.belajar()
Sam.makan()
# memanggil metode induk
Chris.info()
Chris.bekerja()
Chris.makan()
