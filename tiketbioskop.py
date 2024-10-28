# Program Pemesanan Tiket Bioskop
# Harga tiket reguler dan VIP
harga_reguler = 50000
harga_vip = 100000

# Input tipe tiket dari user
tipe_tiket = input("Masukkan tipe tiket (reguler/VIP): ").lower()

# Input status member dari user
member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()

# Menentukan harga tiket berdasarkan tipe tiket
harga = harga_vip if tipe_tiket == "vip" else harga_reguler

# Menghitung diskon jika user adalah member
diskon = 0.2 * harga if member == "ya" else 0

# Menghitung total harga setelah diskon
total_harga = harga - diskon

# Output total harga yang harus dibayar
print(f"Total harga yang harus dibayar: Rp{total_harga}")
