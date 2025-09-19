import math

# NIM sudah diketahui
nim = "250441100125"

# Ambil 3 digit terakhir dan 1 digit terakhir
nim_3 = nim[-3:]
nim_3_int = int(nim_3)
nim_1_int = int(nim[-1])

# 1. Marathon TV series
episode_durasi = 35  # menit
total_episode = 10
total_menit = episode_durasi * total_episode
total_jam = total_menit / 60

print(f"1. Total waktu menonton TV series adalah {total_jam:.2f} jam.")

# 2. Membeli cupang dan koi
harga_cupang = 10000
harga_koi = 20000
uang_bawa = (nim_3_int + 100) * 1000  # Rp.225000

jumlah_cupang = 5
jumlah_koi = 2

total_belanja = (harga_cupang * jumlah_cupang) + (harga_koi * jumlah_koi)
sisa_uang = uang_bawa - total_belanja

print(f"\n2. Uang yang kamu bawa: Rp{uang_bawa:,}")
print(f"   Total belanja: Rp{total_belanja:,}")
print(f"   Sisa uang kamu: Rp{sisa_uang:,}")

# 3. Liburan dengan sepeda motor
jarak_perjalanan = nim_3_int  # KM
konsumsi_bbm = 2.7  # KM per liter
kapasitas_tangki = nim_1_int + 3  # liter
harga_bensin_per_liter = int(f"1{nim_3}0")  # Rp.11250

# Hitung total bensin yang dibutuhkan
total_bensin = jarak_perjalanan / konsumsi_bbm

# Cek diskon
if total_bensin > 3:
    diskon = 500
else:
    diskon = 0

harga_bensin_diskon = harga_bensin_per_liter - diskon
total_biaya_bensin = total_bensin * harga_bensin_diskon

# Hitung berapa kali isi bensin (asumsi tangki penuh setiap isi)
jumlah_isi = math.ceil(total_bensin / kapasitas_tangki)

print(f"\n3. Total bensin yang dibutuhkan: {total_bensin:.2f} liter")
if diskon > 0:
    print(f"   Harga bensin per liter setelah diskon Rp{harga_bensin_diskon:,}")
else:
    print(f"   Harga bensin per liter tanpa diskon Rp{harga_bensin_per_liter:,}")
print(f"   Total biaya bensin: Rp{int(total_biaya_bensin):,}")
print(f"   Perkiraan kali isi bensin: {jumlah_isi} kali (dengan kapasitas tangki {kapasitas_tangki} liter)")