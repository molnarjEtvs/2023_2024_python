def mosogepRogzites():
    markak = []
    while True:
        marka = input("Add meg a mosógép márkát: ")
        if marka == "": #if not marka:
            break
        marka = marka.capitalize()
        markak.append(marka)
    return markak

def mosogepElemezes(markak):
    db = len(markak)
    print(f"Darabszám: {db}db")
    sdb = 0
    for egyElem in markak:
        if egyElem.find("s")>-1 or egyElem.find("S")>-1:
            sdb+=1
    print(f"{sdb} db van s betű")
    szeparator = "/"
    szoveg = szeparator.join(markak)
    print(f"Rögzített mosógépek: {szoveg}")

m = mosogepRogzites()
mosogepElemezes(m)