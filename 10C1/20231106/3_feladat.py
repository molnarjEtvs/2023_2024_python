import random

valasz = input("Add meg hogy lebegőpontos vagy egész számot szeretnél L/E ?")

if valasz == "E":
    szam = random.randint(1,3000)
    print(szam)
elif valasz == "L":
    szam = random.uniform(1,3000)
    print(szam)
else:
    print("Nem értem a válaszod")
