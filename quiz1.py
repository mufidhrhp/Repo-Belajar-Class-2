# 485 hari, nyatakan dalam tahun, bulan, minggu dan hari. 
# 1 bulan = 30 hari, 1 tahun 360 hari

# import math

# a = 485
# tahun = 360
# bulan = 30
# minggu = 7 
# hari = 1

# atahun = math.floor(a/tahun)
# abulan = math.floor((a % tahun) / bulan)
# aminggu = math.floor((a % bulan) / minggu)
# ahari = a - (atahun*tahun) - (abulan*bulan) - (aminggu*minggu)

# print(f'{a} hari sama dengan {atahun} tahun, {abulan} bulan, {aminggu} minggu, {ahari} hari.')

#input

import math

a = int(input('Masukkan hari: '))
tahun = 360
bulan = 30
minggu = 7 
hari = 1

atahun = math.floor(a/tahun)
abulan = math.floor((a % tahun) / bulan)
aminggu = math.floor((a % bulan) / minggu)
ahari = a - (atahun*tahun) - (abulan*bulan) - (aminggu*minggu)

print(f'{a} hari sama dengan {atahun} tahun, {abulan} bulan, {aminggu} minggu, {ahari} hari.')






