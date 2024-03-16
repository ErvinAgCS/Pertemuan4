nilai_a = int(input("Masukan Angka Pertama :"))
nilai_b = int(input("Masukan Angka Kedua   :"))
nilai_c = int(input("Masukan Angka Ketiga  :"))

if nilai_a < nilai_b and nilai_a < nilai_c  :
    print("Hasilnya adalah",nilai_a,"Lebih kecil dari",nilai_b,"dan",nilai_c)
elif nilai_b < nilai_a and nilai_b < nilai_c :
    print("Hasilnya adalah",nilai_b,"Lebih kecil dari",nilai_a,"dan",nilai_c)
elif nilai_c < nilai_a and nilai_c < nilai_b :
    print("Hasilnya adalah",nilai_c,"Lebih kecil dari",nilai_a,"dan",nilai_b)
else:
    print("Semua bilangan sama besar")