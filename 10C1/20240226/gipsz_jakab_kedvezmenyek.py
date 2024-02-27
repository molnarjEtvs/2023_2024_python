hanyEves = input("Add meg hány éves vagy: ")
hanyEves = int(hanyEves)
termekAra = input("Add meg a termék árát: ")
termekAra = int(termekAra)

kedvezmeny = 0
kedvezmenyesAr = 0

if hanyEves>=10 and hanyEves<=14:
    kedvezmeny = 20
elif hanyEves>=15 and hanyEves<=25:
    kedvezmeny = 17.5
elif hanyEves>25 and hanyEves<=35:
    kedvezmeny = 15
else:
    kedvezmeny = 0

kedvezmenyOsszeg = termekAra*(kedvezmeny/100)
kedvezmenyesAr = termekAra-kedvezmenyOsszeg

print(f"A kedvezmény értéke: {kedvezmeny}%")
print(f"A kedvezmény összege: {kedvezmenyOsszeg} Ft")
print(f"A kedvezményes ár: {kedvezmenyesAr} Ft")