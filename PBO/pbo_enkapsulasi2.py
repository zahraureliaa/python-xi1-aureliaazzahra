class Siswa:

    def __init__(self, nis, nama, kelas):
        self.__nis = nis
        self.__nama = nama
        self.__kelas = kelas
    
    # getter
    def getnis(self):
        return self.__nis
    
    # setter
    def setnis(self, newnis):
        self.__nis = newnis
    
aurel = Siswa(16354, "Aurelia Azzahra", "XI MIPA 1")

print(aurel.getnis())
aurel.setnis(10000)
print(aurel.getnis())