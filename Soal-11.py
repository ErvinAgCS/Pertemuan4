jenis_kelamin = "perempuan"
berat_badan = 46
tinggi_badan = 175
usia = 21
nilai_akademis = 89
cek_cacat = False
cek_skill = "TIDAK ADA"

if cek_cacat == True:
    print("Maaf kamu tidak lulus karena cacat.")
       
elif ((jenis_kelamin == "laki-laki" or jenis_kelamin == "perempuan") and (cek_skill == "Menembak" or cek_skill == "Memanah" or cek_skill == "Berkuda")):
    print(f"Kamu lolos dengan jenis kelamin {jenis_kelamin}, karena kamu memiliki skill {cek_skill}.")
    
elif (jenis_kelamin == "perempuan" and (berat_badan >= 45 or berat_badan <= 50) and tinggi_badan >= 165 and (usia >= 15 or usia <= 20)):
    print(f"Kamu lulus, dengan jenis kelamin {jenis_kelamin}, berat badan {berat_badan}, dan tingginya {tinggi_badan} dan usianya {usia} tahun.")

elif ((jenis_kelamin == "laki-laki" or jenis_kelamin == "perempuan") and berat_badan <= 70 and tinggi_badan >= 170 and usia <= 25):
    print(f"Kamu lulus, dengan jenis kelamin {jenis_kelamin}, berat badan {berat_badan} dan tinggIi {tinggi_badan} dan usianya {usia} tahun .")

elif ((jenis_kelamin == "laki-laki" or jenis_kelamin == "perempuan") and nilai_akademis >= 90 and usia <= 30):
    print(f"Kamu lulus, dengan jenis kelamin {jenis_kelamin}, karna nilai rata-rata akademis kamu {nilai_akademis} dan usia {usia} tahun.")
     
else:
    print("Maaf kamu tidak lolos")
