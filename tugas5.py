#1.  FUNCTIONS

def greet(nama: str) -> str:
    return f"Halo, {nama}!"


def tambah(a: float, b: float = 0.0) -> float:
    return a + b


def rata_rata(angka: list[float]) -> float:
    if len(angka) == 0:
        return 0.0
    avg = sum(angka) / len(angka)
    return round(avg, 2)


#2. CLASS

class Student:
    def __init__(self, nama: str, nim: str):
        self.nama = nama
        self.nim = nim
        self.nilai = []

    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        if self.rata_nilai() >= threshold:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    def __str__(self):
        return f"Student(nama='{self.nama}', nim='{self.nim}', rata={self.rata_nilai()}, status={self.status()})"


#3. DEMO

if __name__ == "__main__":
    print("=== FUNCTIONS ===")

    print(greet("Arifian"))

    print("tambah(5, 7):", tambah(5, 7))
    print("tambah(10):", tambah(10))

    print("rata_rata([80, 90, 100]):", rata_rata([80, 90, 100]))
    print("rata_rata([]):", rata_rata([]))


    print("\n=== CLASS STUDENT ===")

    # Mahasiswa 1
    mhs1 = Student("Budi", "A123")
    mhs1.tambah_nilai(80)
    mhs1.tambah_nilai(85)
    mhs1.tambah_nilai(90)

    print(mhs1)
    print("Rata-rata:", mhs1.rata_nilai())
    print("Status:", mhs1.status())

    # Mahasiswa 2
    mhs2 = Student("Siti", "B456")
    mhs2.tambah_nilai(60)
    mhs2.tambah_nilai(65)

    print(mhs2)
    print("Rata-rata:", mhs2.rata_nilai())
    print("Status:", mhs2.status())
