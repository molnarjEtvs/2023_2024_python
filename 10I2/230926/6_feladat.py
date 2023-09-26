

kutyaKor = input("Add meg hány éves a blöki: ")
kutyaKor = int(kutyaKor)

eletkor = 0
for x in range(1,(kutyaKor+1)):
    if x<3:
        eletkor += 10.5
    else:
        eletkor += 4
print(f"A kutya éltekora emberi években: {eletkor}")