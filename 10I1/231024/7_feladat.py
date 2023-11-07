import os
os.system("cls")

szinek = []

while True:
    szin = input("Adj meg egy színt: ")
    if szin == "":
        break
    szinek.append(szin)

db = len(szinek)
print(f"A rögzített színek darabszám: {db} db")
elsoSzin = szinek[0]
print(f"Első elem: {elsoSzin}")
utolsoSzin = szinek[-1]
print(f"Utolsó szín: {utolsoSzin}")
