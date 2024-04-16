def rCharRecords():
    karakaterek = []
    while True:
        karakter = input("Add meg a karakter nevét: ")
        if karakter == "":
            break
        karakter = karakter.upper()
        if karakter not in karakaterek:
            karakaterek.append(karakter)
    return karakaterek

def rCharStatics(karakterLista):
    db = len(karakterLista)
    print(f"Rögzített karakterek száma: {db} db")
    legutolso = max(karakterLista)
    print(f"Legutolsó az ABC-ben: {legutolso}")
    dbME = 0
    for egyKarakter in karakterLista:
        if egyKarakter.startswith("M") == True and egyKarakter.endswith("E") == True:
            dbME += 1
    print(f"M-el kezd és E-re végződik: {dbME} db")
    szeparator = "|"
    szoveg = szeparator.join(karakterLista)
    print(f"{karakterLista}")

k = rCharRecords()
rCharStatics(k)