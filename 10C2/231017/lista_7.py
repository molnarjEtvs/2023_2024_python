import os
os.system("cls")

szinek = []

while True:
    szin = input("Adj meg egy szint: ")
    if szin == "":
       break
    else:
        szinek.append(szin)

print(f"Első szín: {szinek[0]}")
db = len(szinek)
print(f"A színek darabszáma: {db} db")
print(f"Utolsó szín: {szinek[db-1]}")
