class Siswa:

    def __init__(self, nis, nama, kelas):
        self.__nis = nis
        self.__nama = nama
        self.__kelas = kelas

    # decorator
    @property
    def nis(self):
        pass

    #getter
    @nis.getter
    def nis(self):
        return self.__nis
    
    #setter
    @nis.setter
    def nis(self, newnis):
        self.__nis = newnis

aurel = Siswa(16354, "Aurelia Azzahra", "XI MIPA 1")

print(aurel.nis)
aurel.nis = 123456
print(aurel.nis)