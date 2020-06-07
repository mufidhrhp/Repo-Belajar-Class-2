# INI CODING PERTAMA
# print('Hello World')
# print('Hello')


#VARIABEL
#Variabel: Varieables are named values and can store any type of value

# nama_saya = 'Mufid'
# list_nama = ['Andi', 'Budi', 'Caca']
# print(nama_saya)
# print(list_nama)

#jika nama varibel yg muncul yg pada line terakhir
# umur = 32
# umur = 22
# print(umur)

#DATA TYPES IN PYTHON
# 1. Integer : 1,2,3, 1000
# 2. Float : 1.5, 2.7
# 3. String : 'Andi', "Caca", "Dede"
# 4. List : [1,2,'Andi',"Caca", 3]
# 5. Dictionary : {'nama': 'Andi', 'umur':22, 'profesi' : 'guru'}
# 6. Boolean : True or False
# dan kawan-kawan

#Variabel dengan isi value boolean
# jomblo = True
# print(jomblo)

#CARA MENGECEK DATA TYPE
# nama = 'Andi'
# umur = 22
# tinggi = 168.5
# jomblo = False

# print(type(nama))
# print(type(umur))
# print(type(tinggi))
# print(type(jomblo))

# nama = input('Berapa umur Anda?')
# print(nama)

#LATIHAN 1

# nama = input('Nama kamu? : ')
# umur = input('Umur kamu? : ')
# kelamin = input('Kelamin kamu? : ')
# pekerjaan = input('Pekerjaan kamu? : ')
# print('Nama : '+nama)
# print('Umur : ',umur)
# print('kelamin : '+kelamin)
# print('Pekerjaan : ',pekerjaan)

# BISA GUNAKAN ',' JUGA UNTUK MENGGANTIKAN '+'






# usiaAndi = 40
# usiaBudi = 20
# # print(usiaAndi * usiaBudi)
# # print(usiaAndi / usiaBudi)
# # print(usiaAndi + usiaBudi)
# # print(usiaAndi - usiaBudi)
# # print(usiaAndi % usiaBudi) #ini adalah modulus, atau sisa pembagian
# # print(usiaBudi ** 2) #the power of/pangkat


# usiaAndi += 5 
# #usiaAndi = usiaAndi + 5

# usiaBudi -= 10
# #usiaBudi = usiaBudi - 10

# usiaBudi *= 2
# #usiaBudi = usiaBudi * 2

# print(usiaAndi)
# print(usiaBudi)




#LATIHAN APLIKASI PENGHITUNG LUAS PERSEGI PANJANG


# Panjang=int(input('Berapa panjangnya: '))
# Lebar=int(input('Berapa lebarnya: '))
# Luas = Panjang * Lebar

# print('Luas adalah ', Luas)





#MATH MODULE
# import math

# print(math.pi)
# print(math.fabs(-100)) #mengabosultkan angka minus
# print(math.pow(8,2)) # (a,b) a pangkat b
# print(math.sqrt(50))
# print(math.floor(4.7)) #membulatkan kebawah
# print(math.ceil(4.7)) #membulatkan keatas
# print(round(4.6)) #membulatkan sesuai operasi matematika (bawaan python)
# print(round(4.1)) #membulatkan sesuai operasi matematika (bawaan python)




#LATIHAN 2

# umur_total = 49

# rasio_andi = 4
# rasio_budi = 10
# total_rasio = rasio_andi + rasio_budi

# umur_andi = rasio_andi / total_rasio * umur_total
# umur_budi = rasio_budi / total_rasio * umur_total

# tambahan_waktu = 2
# umur_andi_kedepan = umur_andi + tambahan_waktu
# umur_budi_kedepan = umur_budi + tambahan_waktu

# print(int(umur_andi_kedepan))
# print(int(umur_budi_kedepan))

#STRING
# teks = 'Mari kita belajar Data Science'

# print(len(teks)) #jumlah karakter
# print(teks.index('Data')) #Mengetahui posisi index (penghitungan mulai dari 0)
# print(teks.split(' ')) #Memisahkan teks berdasarkan (' ')
# print(teks.capitalize()) #Contoh
# print(teks.upper()) #CONTOH
# print(teks.lower()) #contoh
# print(' '.join(yourList)) # <-menggabungkan list dengan bridge 

###STRING INDEXING###
#[start:stop:step] step: jumlah karakter sekali langkah
# print(teks[1])
# print(teks[2:])
# print(teks[2:10])
# print(teks[0:30:2])
# print(teks[:5]) #until fifth index, stop
# print(teks[:]) #from start til end
# print(teks[::2]) #start from beginning, stop until the end, step every 2
# print(teks[::-1]) #step normal mulai dari belakang
# print(teks[::-2]) #stepnya terbalik, dibaca dari akhir, setiap langkah 2 karakter
# print(teks[1:30:2]) 


###CONVERT STRING TO NUMBERS###
# panjang = input('Masukkan besaran panjang: ')
# lebar = input('Masukkan besaran lebar: ')

# print(panjang+lebar) #penggabungan string
# print(int(panjang)+int(lebar)) 
# print(float(panjang)+float(lebar))


# usia= 22
# nama = 'Andi'

# print(usia+usia)
# print(str(usia)+' ' + nama) #konversi usia (int) menjadi (str)
# print(str(usia)+' ' + str(usia)) #str + str menjadi menggabungan kata bukan operasi matematika


###LATIHAN 3###

# angka = int(input('Silahkan masukkan angka berapapun: '))
# kuadrat = angka ** 2

# print(f'Kuadrat dari {angka} adalah {kuadrat}') #f = format, bermanfaat untuk menyisipkan variabel dalam string





###LATIHAN 4###
# Sebuah perusahaan PT. Sehat Sentosa memiliki 3 cabang pabrik yaitu di Bandung, Semarang, dan Surabaya.
# Setiap cabang memiliki 3 jenis mesin penghasil masker (mesin A, mesin B, mesin C)
# Kapasitas produksi mesin A: 500 masker/hari, mesin B: 300 masker/hari, mesin C: 100 masker/hari
# Semua cabang memiliki 3 jenis mesin, kecuali Semarang (tidak punya mesin B).
# Berapa produksi masker oleh perusahaan Sehat Sentosa selama 1 bulan (30 hari)?

# mesinA = 500
# mesinB = 300
# mesinC = 100

# bandung_perhari = mesinA + mesinB + mesinC
# semarang_perhari = mesinA + mesinC
# surabaya_perhari = mesinA + mesinB + mesinC

# total_perbulan = (bandung_perhari + semarang_perhari + surabaya_perhari) * 30

# print(f'Perusahaan PT. Sehat Sentosa memproduksi {total_perbulan} per bulan')






###~~~String counter~~~###

str1 = "Hello World"
# str_count1 = str1.count('o')  # counting the character “o” in the givenstring
# print("The count of 'o' is", str_count1)

# str_count2 = str1.count('o', 0,5)
# print("The count of 'o' using start/end is", str_count2)


print(str1.count('o'))
















