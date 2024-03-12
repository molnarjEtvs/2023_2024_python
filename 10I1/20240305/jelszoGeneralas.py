import random
def genPass(hossz):
    l="qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM0123456789#&@.|_-"
    lehet = list(l)
    valasztott = random.sample(lehet,hossz)
    sep = ''
    jelszo = sep.join(valasztott)
    return jelszo

j = genPass(10)
print(j)
j = genPass(2)
print(j)
j = genPass(5)
print(j)
