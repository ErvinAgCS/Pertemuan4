alas = float(input("Masukan luasnya : "))
tinggi = float(input("Masukan kelilingnya : "))

sisi_a = 20
sisi_b = 15
sisi_c = 10

rumus_luas = 1 / 2 * alas * tinggi
s = (sisi_a + sisi_b + sisi_c) / 2 

print(f"Hasil luas segitiga dengan alas {alas:.0f} cm dan tinggi {tinggi:.0f} cm adalah {rumus_luas:.2f} cm².")
print(f"Hasil keliling dengan menggunakan rumus heron adalah {s} cm².")