import os
os.system("cls")

szinek = []

while True:
    szin = input("Adj meg egy színt: ")
    if szin == "":
        break
    szinek.append(szin)

db = len(szinek)
elso = szinek[0]
utolso = szinek[db-1]
print(f"Darabszám: {db}")
print(f"Első szín: {elso}")
print(f"Utolsó szín: {utolso}")
