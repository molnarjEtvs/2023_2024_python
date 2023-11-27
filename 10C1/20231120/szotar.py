import os
os.system("cls")

szotar = {}
while True:
    kulcs = input("Add meg a kulcsot: ")
    if kulcs == "":
        break
    ertek = input("Add meg az értéket: ")
    szotar[kulcs] = ertek

print(szotar)