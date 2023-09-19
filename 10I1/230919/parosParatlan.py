
szam = input("Add meg a számot: ")
szam = int(szam)

if szam>0 and szam%2==0:
    print("pozitív Páros")
elif szam>0 and szam%2!=0:
    print("pozitív PÁRATLAN")
elif szam<0 and szam%2==0:
    print("Negatív Páros")
elif szam<0 and szam%2!=0:
    print("Negatív Páratlan")
else:
    print("0")