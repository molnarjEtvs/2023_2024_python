import os
os.system("cls")


markak = []

while True:
    marka = input("Adj meg egy márkát: ")
    if marka == "":
        break
    markak.append(marka)

markak.remove("adidas")
markak.remove("reebok")

print(f"a márkák listjája {markak}")
