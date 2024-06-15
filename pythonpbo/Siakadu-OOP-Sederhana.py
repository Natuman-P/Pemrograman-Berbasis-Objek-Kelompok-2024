class MataKuliah:
    def __init__(self, nama, sks):
        self.nama = nama
        self.sks = sks

class Dosen:
    def __init__(self, nama):
        self.nama = nama
    
    def validasi_krs(self, krs):
        total_sks = sum([mk.sks for mk in krs.mata_kuliah])
        if 18 <= total_sks <= 22:
            print(f"Dosen {self.nama} memvalidasi KRS {krs.nama}")
        else:
            print(f"Jumlah SKS tidak valid. Total SKS adalah {total_sks}")

class KRS:
    def __init__(self, nama):
        self.nama = nama
        self.mata_kuliah = []

    def tambah_mata_kuliah(self, mata_kuliah):
        if mata_kuliah.sks + sum([mk.sks for mk in self.mata_kuliah]) <= 22:
            self.mata_kuliah.append(mata_kuliah)
            print(f"Mata kuliah {mata_kuliah.nama} berhasil ditambahkan ke dalam KRS {self.nama}")
        else:
            print(f"Tidak dapat menambahkan mata kuliah {mata_kuliah.nama}. SKS melebihi batas maksimal.")

    def total_sks(self):
        total_sks = sum([mk.sks for mk in self.mata_kuliah])
        print(f"Total SKS yang diambil dalam KRS {self.nama} adalah {total_sks}")



class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama
        self.krs = None

    def isi_krs(self, krs):
        self.krs = krs
        print(f"Mahasiswa {self.nama} telah mengisi KRS {krs.nama}")

    def tampilkan_krs(self):
        for x in self.krs.mata_kuliah:
            print(x.nama)


# Contoh penggunaan:
dosen = Dosen("Raden Arum Setia Priadi")
krs = KRS("KRS2024")
mahasiswa = Mahasiswa("Iqbal")

# Daftar mata kuliah dengan SKS
daftar_mata_kuliah = [
    MataKuliah("Pemrograman Berbasis Objek", 3),
    MataKuliah("Sistem Tertanam", 4),
    MataKuliah("Pemrograman Web", 3),
    MataKuliah("Kecerdasan Buatan", 2),
    MataKuliah("Technoprenurship", 2),
    MataKuliah("Sistem Basis Data", 3),
    MataKuliah("Jaringan Komputer", 3),
    MataKuliah("Statistika", 2)
]

# Otomatisasi pengisian KRS
for mk in daftar_mata_kuliah:
    krs.tambah_mata_kuliah(mk)

mahasiswa.isi_krs(krs)

dosen.validasi_krs(krs)

mahasiswa.tampilkan_krs()

krs.total_sks()
