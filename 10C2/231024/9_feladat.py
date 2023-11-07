import os
os.system("cls")

markanevek = []

while True:
    markanev = input("Adj meg egy márkanevet: ")
    if markanev == "":
        break
    markanevek.append(markanev)

markanevek.remove("adidas")
markanevek.remove("reebok")
print(markanevek)