

kutyaKor = input("Add meg hány éves a blöki: ")
kutyaKor = int(kutyaKor)

emberiEv = 0
for kor in range(1,(kutyaKor+1)):
    if kor<3:
        emberiEv += 10.5
    else:
        emberiEv += 4
print(f"Emberi évben a kutya kora: {emberiEv}")