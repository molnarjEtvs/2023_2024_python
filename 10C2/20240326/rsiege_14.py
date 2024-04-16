def rCharRecords():
    karakterek = []
    while True:
        karakter = input("Add meg a karakter nevét: ")
        if karakter == "":
            break
        karakter = karakter.upper()
        if karakter not in karakterek:
            karakterek.append(karakter)
    return karakterek

def rCharStatics(jatekosok):
    db = len(jatekosok)
    print(f"Rögzített karakterek száma: {db} db")
    legutolsoAbc = max(jatekosok)
    print(f"Legutolsó az ABC-ben: {legutolsoAbc}")
    dbME = 0
    for egyJatekos in jatekosok:
        if egyJatekos.startswith("M") == True and egyJatekos.endswith("E") == True:
            dbME+=1

    print(f"M-el kezd és E-re végződik: {dbME} db")
    szeparator = "|"
    szoveg = szeparator.join(jatekosok)
    print(f"{szoveg}")

h = rCharRecords()
rCharStatics(h)