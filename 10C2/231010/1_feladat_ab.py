import os
os.system("cls")

bruttoFizetes = input("Add meg a bruttó fizetésed: ")
bruttoFizetes = int(bruttoFizetes)

eltekor = input("Add meg az életkorod: ")
eltekor = int(eltekor)

'''
B csoport:
nyugger = input("Nyugdíjas vagy (i/n): ")
'''

tb = bruttoFizetes*0.185
szja = bruttoFizetes*0.15

if eltekor<25:
    szja = 0

'''
B csoport:
if nyugger=="i":
    szja = 0
'''

netto = bruttoFizetes-tb-szja

print(f"A nettó fizetésed: {netto} Ft")
print(f"Levont SZJA: {szja} Ft")
print(f"Levont TB: {tb} Ft")
