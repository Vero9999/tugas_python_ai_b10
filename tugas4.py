# 1. List (Akses & manipulasi)
data = ["apple", 10, "banana", 3.14, "cherry", 20] #list
data[0] #elemen pertama > apple
data[-1] #elemen terakhir > 20
data[1:5:2] #slicing > start:stop:step, start = mulai dari index 0 (elemen ke-1) , stop = berhenti sebelum index 5, step = ambil data di posisi sekarang +2   

before = data.copy()
data.append("orange") #tambah di akhir
data.insert(1,"grape") #sisipkan di posisi 1
data.extend(["melon",99]) #gabung dengan list lain

data.pop() #hapus elemen terakhir

data.remove("banana") #hapus banana

print("Before:", before) #print sebelum manipulasi

print("After:"), data) #print setelah manipulasi

#2. Tuple (immutability & unpacking)
tup = ("A", "B", "C", "D", "E") #mirip list, tapi tidak bisa diubah
print("Tuple:", tup)
print("Length:", len(tup)) $jumlah karakter
print("Index2:", tup[2]) #elemen index ke-2 > C
a, b, c, *rest = tup #unpacking, memecah tuple ke dalam variabel

print("Rest:", rest) #sisa elemen > D, E

#3. Set (operasi himpunan)
set1 = {1,2,3,4,5,5}
set2 = {4,5,6,7,8}

print("Set 1:", set1)
print("Set 2:", set2)

print("Union:", set1 | set2) #Union, | , gabungkan semua
print("Intersection:", set1 & set2) #Intersection, &, yang berisisan atau sama atau yang ada di keduanya 
print("Difference:", set1 - set2) #Difference, - , yang ada di set1 tapi tidak ada di set2
print("Symmetric Difference:", set1 ^ set2) #Symmertic Dif, ^ , yang tidak ada di keduanya

#4. Dictionary : menyimpan data dalam format key = value
mahasiswa = {
  "nama":"Eco",
  "nim":"00001",
  "angkatan":2019,
  "kota":"Batam"
}

print("Original:", mahasiswa)

mahasiswa["jurusan"] = "Sisten Informasi" #tambah key baru
mahasiswa ["kota"] = "Jakarta" #mengubah value
del mahasiswa["angkatan"] #menghapus key

print("updated:", mahasiswa)
print("Keys:", mahasiswa.keys()) #semua key yang ada
print("Values:", mahasiswa.values()) #semua value yang ada
print("Items:", mahasiswa.items()) #pasangan key = value
print("Iterasi:") #looping
for k, v in mahasiswa.items():
  print(f"{k}:{v}") #k = key, v = value , tampilkan pasangan key dan valuenya

#5. Nested structure = struktur dalam struktur, contoh : List yang berisi dictionary
books = [
  {"judul":"Book A", "penulis":"Author 1", "tahun":2018},
  {"judul":"Book B", "penulis":"Author 2", "tahun":2021},
  {"judul":"Book B", "penulis":"Author 3", "tahun":2015},
  {"judul":"Book B", "penulis":"Author 3", "tahun":2023}
]

print("Judul buku:")
for book in books:
  print(book["judul"]) #akses judul buku satu per satu

filtered = [b for b in books if b["tahun"] >= 2020]
print("Buku >= 2020:", filtered) #filter hanya buku tahun diatas sama dengan tahun 2020

#6. Comprehension
nums = list(range(1,21)) #himpunan angka dari 1 sd 20
genap = [n for n in nums if n % 2 == 0] #ambil yang genap saja 
kuardrat = [n**2 for n in nums] #kuardratkan semua

print("Genap:", genap)
print("Kuardrat:", kuardrat)

dict_comp = {n: "genap" if n % 2 == 0 else "ganjil" for n in range(1,11)} #dictionary ganjil genap
print("Dict:", dict_comp)

kalimat = "Hello World Pythong"
set_comp = {c.lower() for c in kalimat if c.isalpha()} 
print("Huruf unik:", set_comp) #himpunan huruf unik (tanpa duplikat, tanpa spasi)

#7. Keanggotaan & pencarian
print("Apakah 'apple' ada di list?", "apple" in data)
print("Apakah 10 ada di set?", 10 in set)
if "apple" in data:
  print("Posisi 'apple':", data.index("apple"))
slse:
  print("'apple' tidak ditemukan") #cari posisi value




























