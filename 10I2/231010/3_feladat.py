import os
os.system("cls")

hanykm = input("Add meg hány km: ")
hanykm = int(hanykm)

ar = input("Add meg a 100km-ti árat: ")
ar = int(ar)

utikoltseg = 0

for x in range(1,hanykm+1):
    if x%3==0 and x%5==0:
        utikoltseg += (ar/100)*(x*2)
    else:
        utikoltseg += (ar/100)*x

print(f"Utiköltség: {utikoltseg} Ft")