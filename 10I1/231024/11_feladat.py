import os
os.system("cls")

szamok1 = [3, 45, 10,  8, 324, 56,  23, 45,  98, 777,  678, 83, 65,  98, 4,  7, 65, 10, 98, 3, 23,  53,  16, 763,  9, 495, 6,  7, 87, 53, 165,  34, 79, 52, 36, 77,  521, 243, 34, 56,  765, 34,  23, 125, 7,  5, 34,  8, 234,  31, 3]
szamok2 = [3,45,10,8,324,56,23,45,98,777,678,83,65,98,4,7,65,10,98,3,23,53,16,763,9,465,6,7,87,53,165,34,79,79,52,10,8,77,521,243,34,56,765,10,23,125,7,5,6,34,8,234,31,3]


db1 = len(szamok1)
db2 = len(szamok2)

if db1>db2:
    print("Az első listában van több elem")
elif db1<db2:
    print("A második listában van több elem")
else:
    print("Egyforma az elemek száma")

tizes1 = szamok1.count(10)
tizes2 = szamok2.count(10)

if tizes1>tizes2:
    print("Az első listában van több 10")
elif tizes1<tizes2:
    print("A második listában van több 10")
else:
    print("Egyforma a 10-ek száma")

atlag1 = sum(szamok1)/len(szamok1)
atlag2 = sum(szamok2)/len(szamok2)


if atlag1>atlag2:
    print("Az első listának több az átlaga")
elif atlag1<atlag2:
    print("A második listának több az átlaga")
else:
    print("Egyforma a két lista átlaga")