import os
os.system("cls")

bruttoFizetes = input("Add meg a bruttó fizetésed: ")
bruttoFizetes = int(bruttoFizetes)
szja = bruttoFizetes*0.15
tb = bruttoFizetes*0.185
szocho = bruttoFizetes*0.13
netto = bruttoFizetes-szja-tb
munkaltatoKoltseg = bruttoFizetes+szocho

print(f"A nettó fizetésed: {netto} Ft")
print(f"Levonásra kerül:")
print(f"Szja: {szja}")
print(f"Tb: {tb}")
print(f"Ez a munkáltatódnak {munkaltatoKoltseg} Ft-ba került.")