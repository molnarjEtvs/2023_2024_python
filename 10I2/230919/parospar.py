szam = input("Adj meg egy számot:")
szam = int(szam)

if szam>0 and szam%2==0:
    print("Pozitív Páros")
elif szam<0 and szam%2==0:
    print("Negatív Páros")
elif szam>0 and szam%2>0:
    print("Pozitív Páratlan")
elif szam<0 and szam%2>0:
    print("Negatív Páratlan")
else:
    print("0")