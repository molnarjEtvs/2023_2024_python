import os
os.system("cls")

kw = input("Add meg az éves fogyasztást kw-ban: ")
kw = int(kw)
db = input("Add meg a mosások számát: ")
db = int(db)
aramdij = 40

if aramdij <= 0 or db <= 0:
    print("Sajnos ezekkel az adatokkal nem tudok számolni.")
else:
    aramIgeny = kw/db
    aramKoltseg = aramIgeny*aramdij
    print(f"Egy mosás áramköltsége: {aramKoltseg} Ft")
