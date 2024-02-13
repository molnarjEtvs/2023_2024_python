import os
os.system("cls")

bruttoFizetes = input("Add meg a bruttó fizetést: ")
bruttoFizetes = int(bruttoFizetes)

szja = bruttoFizetes*0.15
tb = bruttoFizetes*0.185
szocho = bruttoFizetes*0.13
nettoFizetes = bruttoFizetes-szja-tb
munkaltatoiKoltseg = bruttoFizetes+szocho

print(f"A nettó fizetésed: {nettoFizetes} Ft")
print(f"Levonsára kerül: ")
print(f"Szja: {szja}")
print(f"Tb: {tb}")
print(f"Ez a munkáltatódnak {munkaltatoiKoltseg} Ft-ba került.")
