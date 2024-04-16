def mosogepRogzites():
    marakak = []
    while True:
        marka = input("Add meg a mosógép márkáját: ")
        if marka == "": #if not marka:
            break
        marka = marka.capitalize()
        marakak.append(marka)
    return marakak

def mosogepElemzes(lista):
    db = len(lista)
    print(f"Darabszám: {db}db")
    sdb = 0
    for elem in lista:
        if elem.find("s")>-1 or elem.find("S")>-1:
            sdb += 1 #sdb = sdb+1
    print(f"{sdb}db s betűs van")
    szeparator = "/"
    szovegesen = szeparator.join(lista)
    print(f'Rögzített mosógépek: {szovegesen}')

mosogepek = mosogepRogzites()
mosogepElemzes(mosogepek)