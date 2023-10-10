import os
os.system("cls")

hanyKm = input("Hány km-t utazol? ")
hanyKm = int(hanyKm)

benzinAr = input("Add meg a benzin literenkénti árát: ")
benzinAr = int(benzinAr)

utazasiKoltseg = 0

for x in range(1,(hanyKm+1)):
    if x%3==0 and x%5==0: #B: if x%4==0 and x%6==0:
        utazasiKoltseg += (benzinAr/100)*(x*2)
    else:
        utazasiKoltseg += (benzinAr/100)*x
print(f"Utazási költség: {utazasiKoltseg} Ft")