import os
os.system("cls")

gyumolcsok = []

while True:
    gyumi = input("Adj meg egy gyümölcöt: ")
    if gyumi == "":
        break
    gyumi = gyumi.capitalize()
    gyumolcsok.append(gyumi)

print(gyumolcsok)

