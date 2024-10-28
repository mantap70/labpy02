# Program Kalkulator Sederhana
# Input dua angka dari user
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Input operator aritmatika dari user
operator = input("Masukkan operator (+, -, *, /): ")

# Menghitung hasil berdasarkan operator yang dipilih
if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "*":
    hasil = angka1 * angka2
elif operator == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        hasil = "Error: Pembagian dengan nol tidak diperbolehkan."
else:
    hasil = "Operator tidak valid."

# Output hasil perhitungan
print(f"Hasil: {hasil}")
