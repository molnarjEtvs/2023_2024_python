import os
os.system("cls")

def bekeres():
    szavak = []
    while True:
        szo = input("Add meg a szót: ")
        if szo == "":
            break
        szavak.append(szo)
    return szavak

def megallapitas(szavak):
    db = len(szavak)
    elsoSzo = szavak[0]
    utolsoSzo = szavak[-1]
    print(f"Darabszám: {db} db")
    print(f"Első szó: {elsoSzo}")
    print(f"Utolsó szó: {utolsoSzo}")

sz = bekeres()
megallapitas(sz)