import os
os.system("cls")

kw = input("Add meg az éves fogyasztást kw-ban: ")
db = input("Add meg a mosások számát: ")
aramdij = 40

if kw<=0 or db<=0:
    print("Sajnos ezekkel az adatokkal nem tudok számolni!")
else:
    mosasAramigeny = kw/db
    aramkoltseg = mosasAramigeny*aramdij
    print(f"Egy mosás áramköltsége: {aramkoltseg} Ft")


