import os 
os.system("cls")

bruttoFizetes = input("Add meg a brutto fizetést: ")
bruttoFizetes = int(bruttoFizetes)

szja = bruttoFizetes*0.15
tb = bruttoFizetes*0.185

eletkor = input("Add meg az életkorod: ")
eletkor = int(eletkor)

if eletkor<25:
    szja = 0

netto = bruttoFizetes-szja-tb
print(f"Nettó fizetés: {netto} Ft")
print(f"LEVONT SZJA: {szja} Ft")
print(f"Levont TB: {tb} Ft")