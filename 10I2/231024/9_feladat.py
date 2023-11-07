import os
os.system("cls")

markanevek = []

while True:
    marknev = input("Adj meg egy márkanvet: ")
    if marknev == "":
        break
    markanevek.append(marknev)

markanevek.remove("reebok")
markanevek.remove("adidas")

print(markanevek)
