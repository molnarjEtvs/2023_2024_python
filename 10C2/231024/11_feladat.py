import os
os.system("cls")

szamok1 = [3, 45, 10,  8, 324, 56,  23, 45,  98, 777,  678, 83, 65,  98, 4,  7, 65, 10, 98, 3, 23,  53,  16, 763,  9, 495, 6,  7, 87, 53, 165,  34, 79, 52, 36, 77,  521, 243, 34, 56,  765, 34,  23, 125, 7,  5, 34,  8, 234,  31, 3]
szamok2 = [3,45,10,8,324,56,23,45,98,777,678,83,65,98,4,7,65,10,98,3,23,53,16,763,9,465,6,7,87,53,165,34,79,79,52,10,8,77,521,243,34,56,765,10,23,125,7,5,6,34,8,234,31,3]

db1 = len(szamok1)
db2 = len(szamok2)

tiz1 = szamok1.count(10)
tiz2 = szamok2.count(10)

atlag1 = sum(szamok1)/db1
atlag2 = sum(szamok2)/db2

if db1>db2:
    print("Az elsőben van több elem")
elif db1<db2:
    print("A második listában van több elem")
else:
    print("Ugyanannyi elem van")

if tiz1>tiz2:
    print("Az elsőben van több 10")
elif tiz1<tiz2:
    print("A második listában van 10")
else:
    print("Ugyanannyi 10 van mind kettőben")

if atlag1>atlag2:
    print("Az első listának nagyobb az átlaga")
elif atlag1<atlag2:
    print("A második listának nagyobb az átlaga")
else:
    print("A két lista átlaga egyenlő")

