import os 
os.system("cls")

vegosszeg = 0
befizetes = 0
while befizetes != -2:
    befizetes = input("Add meg a befizetett összeget: ")
    befizetes = int(befizetes)
    if befizetes>0:
        vegosszeg += befizetes
print(f"A befizetett összeg: {vegosszeg} Ft")