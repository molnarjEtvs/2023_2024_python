szam1 = input("Adjon meg 1 szamot: ")
szam1 = int(szam1)
szam2 = input("Adjon meg 1 szamot: ")
szam2 = int(szam2)
for x in range(szam1,szam2+1):
    if x%2==0:
        print(x)