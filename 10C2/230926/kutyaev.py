

kutyakor = input("Add meg hány éves a blöki: ")
kutyakor = int(kutyakor)
emberiEvekben = 0

for ev in range(1,(kutyakor+1)):
    if ev<3:
        emberiEvekben += 10.5
    else:
        emberiEvekben += 4
print(f'A kutya emberi években: {emberiEvekben} éves.')