
valtasMod = input("Add meg a váltás módját (FC/CF): ")
ertek = input("Add meg az átváltandó értéket: ")
ertek = float(ertek)

if valtasMod == "FC":
    celsius = (5*(ertek-32))/9
    print(f"{ertek} F => {celsius} C")
elif valtasMod == "CF":
    faren = (9*ertek+(32*5))/5
    print(f"{ertek} C => {faren} F")
else:
    print("Nem értem amit írsz") 