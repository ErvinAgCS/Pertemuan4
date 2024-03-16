bilangan = int(input("Masukan bilangan anda: "))

if bilangan % 2 == 0 and bilangan >= 1:
    print("Bilangan ini adalah Genap Positif.")
elif bilangan % 2 == 1 and bilangan >= 1:
    print("Bilangan ini adalah Ganjil Positif")
    
elif bilangan % 2 == 0 and bilangan < 0 :
    print("Bilangan ini adalah Genap Negatif.")
elif bilangan % 2 == 1 and bilangan < 0:
    print("Bilangan ini adalah Ganjil Negatif")
    
else:
    print(f"bilangan ini adalah ",bilangan)