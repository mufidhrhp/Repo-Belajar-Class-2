# CONDITION (IF, ELIF, ELSE)

# nilai = int(input('Masukkan nilai siswa: '))

# if nilai > 80:
#     print('Excellent')

# elif nilai >=60 and nilai <=80:
#     print('Good job!')

# else:
#     print("Don't give up")






#CONDITION JENIS DATANYA BOOLEAN
# jomblo = True

# if jomblo:
#     print('Masih jomblo')

# else:
#     print('Taken')




# angka = int(input('Masukkan angka : '))

# if angka %2 == 0: #INGAT pakai '==' karena '=' untuk menentukan variebel!
#     print(f'Angka {angka} tergolong bilangan GENAP!')

# else:
#     print(f'Angka {angka} tergolong bilangan GANJIL!')



###LATIHAN 5###

# massa = int(input('Masukkan Massa (kg) :'))
# tinggi = int(input('Masukkan Tinngi (cm) :'))
# tinggiM = tinggi/100

# imt = massa / tinggiM**2

# if imt < 18.5:
#     print (f'Massa {massa}kg & tinggi {tinggiM} M')
#     print (f'IMT = {imt}, Berat badan KURANG')

# elif imt >= 18.5 and imt <= 24.9:
#     print (f'Massa {massa}kg & tinggi {tinggiM} M')
#     print (f'IMT = {imt}, Berat badan IDEAL')

# elif imt >= 25.0 and imt <= 29.9:
#     print (f'Massa {massa}kg & tinggi {tinggiM} M')
#     print (f'IMT = {imt}, Berat badan BERLEBIH')

# elif imt >= 30 and imt <= 39.9:
#     print (f'Massa {massa}kg & tinggi {tinggiM} M')
#     print (f'IMT = {imt}, Berat badan SANGAT BERLEBIH')

# else:
#     print (f'Massa {massa}kg & tinggi {tinggiM} M')
#     print (f'IMT = {imt}, Berat badan OBESITAS')


# GABNJIL GENAP

# nilai = int(input('Masukan Angka: '))
# if nilai % 2 == 0:
#     print(f'Angka {nilai} tergolong bilangan GENAP')
# else:
#     print(f'Angka {nilai} tergolong bilangan GANJIL')






###~~~LATIHAN 6~~~~###

import math

vA=60
vB=40
jam = 9
jarak=120


waktutabrak = jarak/(vA + vB)

jamtabrak = jam + waktutabrak

print('Pukul', math.floor(jamtabrak), 'lebih', round((waktutabrak - math.floor(waktutabrak)) * 60), 'menit')







