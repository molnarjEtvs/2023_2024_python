import os
os.system("cls")

bruttoFizetes = input("Add meg a bruttó fizetésed: ")
bruttoFizetes = int(bruttoFizetes)

nyugger = input("Nyugdíjas vagy-e (i/n): ")

tb = bruttoFizetes*0.185
szja = bruttoFizetes*0.15

if nyugger=='i':
    szja = 0

netto = bruttoFizetes-tb-szja

print(f"A nettó béred: {netto} Ft")
print(f"Levont SZJA: {szja} Ft")
print(f"Levon TB: {tb} Ft")

