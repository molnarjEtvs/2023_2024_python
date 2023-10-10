import os
os.system("cls")

osszeg = 0
befizetes = 0

while befizetes != -1:
    befizetes = input("Add meg a befizetett összeget: ")
    befizetes = int(befizetes)
    if befizetes>0:
        osszeg += befizetes
print(f"BEfizetett összeg: {osszeg} Ft")