import os
os.system("cls")

def bekeres():
    szavak = []
    while True:
        szo = input("Adj meg egy szót: ")
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

x = bekeres()
megallapitas(x)