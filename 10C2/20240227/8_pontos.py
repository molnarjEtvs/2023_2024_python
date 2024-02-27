kor = input("Add meg hány éves vagy: ")
kor = int(kor)
ar = input("Add meg a termék árát: ")
ar = int(ar)

#kor>=10 and <=14
if kor>=10 and kor<=14:
    kedvezmeny = 20
elif kor>=15 and kor <=25:
    kedvezmeny = 17.5
elif kor>25 and kor<=35:
    kedvezmeny = 15
else:
    kedvezmeny = 0

kedvezmenyOsszege = ar(kedvezmeny/100)
kedvezmenyesAr = ar-kedvezmenyOsszege

print(f"A kedvezmény értéke: {kedvezmeny}%")
print(f"A kedvezmény összege: {kedvezmenyOsszege} Ft")
print(f"A kedvezményes ár: {kedvezmenyesAr} Ft")

