#1. Variabel & tipe data
name = "Eco" #srting (teks)
age = 36 #integer (bilangan bulat)
height = 165.5 #float (bilangan desimal)
is_student = True #boolean (t/f)
hobbies = ["reading","gaming","travelling"] #list (kumpulan data)

#2. Manipulasi string
greeting = "Hello"
full_text = greeting + " " + name #concatenation (menggabungkan string)
print(full_text) 
print("Length on name:", len(name)) #menghitung jumlah karakter
print("Uppercase:", name,upper()) #ubah ke huruf besar
print("Lowercase:", name,lower()) #ubah ke huruf kecil

#3. Operasi matematika
a = 10
b = 3
print("Addition:", a + b) #tambah
print("Substraction:", a - b) #kurang
print("Multiplication:", a * b) #kali
print("Division:", a / b) #bagi
print("Floor division:", a // b) #bagi, hasil bulatkan kebawah
print("Modulus:", a % b) #sisa bagi

#4. List & akses elemen
print("Original hobbies:", hobbies)
print("First Hobby:", hobbies[0]) #ambil elemen pertama > reading
print("Last Hobby:", hobbies[-1]) #ambil elemen terakhir > travelling

hobbies.append("sleeping") #tambah elemen di akhir
print("After append:", hobbies) 

hobbies.remove("gaming") #habus elemen berdasarkan kriteria
print("After remove:", hobbies)

hobbies.pop() #hapus elemen terakhir
print("After pop:", hobbies)

# 5. Input User
user_name = input("Masukkan nama Anda:") #instruksi mengisikan nama
user_age = input("Masukkan umur Anda:") #instruksi mengisikan umur
print(f"Haiiii, nama saya {user_name} dan umur saya {user_age} tahun.") #f string untuk menyisipkan variabel dalam teks 






