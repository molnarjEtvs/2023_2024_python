import os
os.system("cls")

etelek = []

for i in range(5):
    etel = input("Adj meg egy ételt: ")
    etelek.append(etel)

etelek.pop(2)
etelek.insert(3,"Töltött káposzta")

sorszam = 1
for etel in etelek:
    print(f"{sorszam}.{etel}")
    sorszam+=1