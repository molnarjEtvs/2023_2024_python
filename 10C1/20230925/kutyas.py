
kutyaKora = input("Add meg hány éves a kutyád: ")
kutyaKora = int(kutyaKora)

kutyaEmberiEvekben = 0
for x in range(1,(kutyaKora+1)):
    if x<=2:
        kutyaEmberiEvekben += (x*10.5)
    else:
        kutyaEmberiEvekben += x*4
print(f"A kutyád emberi években számolva: {kutyaEmberiEvekben} éves")
