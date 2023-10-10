import os
os.system("cls")
bruttoFizetes = input("Add meg mennyi a bruttó fizetésed: ")
bruttoFizetes = int(bruttoFizetes)

eletkor = input("Add meg az életkorod: ")
eletkor = int(eletkor)

tb = bruttoFizetes*0.185
szja = bruttoFizetes*0.15

if eletkor<25:
    szja = 0
netto = bruttoFizetes-tb-szja

print(f"A nettó fizetésed: {netto} Ft")
print(f"Levont szja: {szja} Ft")
print(f"Levont TB: {tb} Ft")