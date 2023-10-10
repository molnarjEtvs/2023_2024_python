import os
os.system("cls")

befizetes = 0
zsebpenz = 0
while befizetes != -1:
    befizetes = input("Add meg a befizetett összeget: ")
    befizetes = int(befizetes)
    if befizetes>0:
        zsebpenz = zsebpenz+befizetes
print(f"Teljes összeg: {zsebpenz} Ft")