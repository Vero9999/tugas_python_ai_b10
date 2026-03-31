#1. IMPORT & SETUP
import numpy as np
import pandas as pd
import os

np.random.seed(42)


#2. NUMPY – DATA & STATISTIK
nilai_array = np.random.randint(50, 100, size=10)

rata2 = np.mean(nilai_array)
median = np.median(nilai_array)
std_dev = np.std(nilai_array)
nilai_min = np.min(nilai_array)
nilai_max = np.max(nilai_array)


#3. PANDAS – DATAFRAME
data = {
    "nama": ["Budi", "Siti", "Andi", "Rina", "Dewi"],
    "nim": ["A001", "A002", "A003", "A004", "A005"],
    "nilai": nilai_array[:5]
}

df = pd.DataFrame(data)

# tambah kolom status
df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")


#4. FILE I/O
def write_summary(path: str):
    with open(path, "w") as f:
        f.write("=== RINGKASAN STATISTIK ===\n")
        f.write(f"Rata-rata: {rata2:.2f}\n")
        f.write(f"Median: {median:.2f}\n")
        f.write(f"Std Dev: {std_dev:.2f}\n")
        f.write(f"Min: {nilai_min}\n")
        f.write(f"Max: {nilai_max}\n\n")

        f.write("=== RINGKASAN DATAFRAME ===\n")
        f.write(f"Jumlah data: {len(df)}\n")
        f.write(f"LULUS: {(df['status'] == 'LULUS').sum()}\n")
        f.write(f"TIDAK LULUS: {(df['status'] == 'TIDAK LULUS').sum()}\n")


#5. OOP – GRADEBOOK
class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return float(self.df["nilai"].mean())

    def pass_rate(self, threshold: float = 70.0) -> float:
        total = len(self.df)
        passed = (self.df["nilai"] >= threshold).sum()
        return round((passed / total) * 100, 2)

    def save_summary(self, path: str):
        with open(path, "a") as f:  # append
            f.write("\n=== GRADEBOOK SUMMARY ===\n")
            f.write(f"Average: {self.average():.2f}\n")
            f.write(f"Pass Rate: {self.pass_rate()}%\n")

    def __str__(self):
        return f"GradeBook(total={len(self.df)}, average={self.average():.2f})"


#6. DEMO
if __name__ == "__main__":

    print("=== NUMPY ===")
    print("Array:", nilai_array)
    print("Mean:", rata2)
    print("Median:", median)
    print("Std Dev:", std_dev)
    print("Min:", nilai_min)
    print("Max:", nilai_max)

    print("\n=== PANDAS ===")
    print(df.head())

    print("\n=== OOP: GRADEBOOK ===")
    gb = GradeBook(df)

    print(gb)
    print("Average:", gb.average())
    print("Pass Rate:", gb.pass_rate(), "%")

    file_path = "ringkasan_tugas6.txt"

    # tulis file awal
    write_summary(file_path)

    # tambah dari class
    gb.save_summary(file_path)

    print(f"\nRingkasan disimpan ke: {file_path}")
