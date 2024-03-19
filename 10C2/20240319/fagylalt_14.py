def fagylaltNevek():
    fagyik = []
    while True:
        nev = input("Add meg a fagyi nevét: ")
        if nev == "":
            break
        nev = nev.capitalize()
        fagyik.append(nev)
    return fagyik

def Statisztika(f):
    db = len(f)
    dbVegan = 0
    print(f"{db} féle fagylalt kapható.")
    for egy in f:
        if egy.find("vegán")>-1 or egy.find("Vegán")>-1:
            dbVegan += 1
    print(f"Ebből vegán ízesítésű {dbVegan} db")

h = fagylaltNevek()
Statisztika(h)