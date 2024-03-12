import random
def genPass(hossz):
    lehetosegek = "qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM0123456789<>#&@"
    lehetLista = list(lehetosegek)
    titkosJelszo = random.sample(lehetLista,hossz)
    sep = ""
    titkosJelszoRet = sep.join(titkosJelszo)
    return titkosJelszoRet

j = genPass(10)
print(j)

db = input("Add meg hány karakter hosszan: ")
db = int(db)
j = genPass(db)
print(j)
