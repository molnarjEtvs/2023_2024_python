import random
def jelszo(hossz):
    lehetosegekSzoveg = "qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM.?#&@"
    lehetosegek = list(lehetosegekSzoveg)
    
    titkosJelszo = random.sample(lehetosegek,hossz)
    sep = ''
    titkosJelszo2 = sep.join(titkosJelszo)
    return titkosJelszo2


j = jelszo(8)
print(j)

h = input("Add meg a hosszt: ")
h = int(h)
j = jelszo(h)
print(j)
