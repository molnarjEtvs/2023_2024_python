
tipus = input("Add meg hogyan váltasz (FC/CF): ")
hom = input("Add meg az értéket: ")
hom = float(hom)

if tipus == "FC":
    c = (5*(hom-32))/9
    print("Celsiusban: {c}C")
elif tipus == "CF":
    f = (9*hom+(32*5))/5
    print("Fareinheit: {f}F")
else:
    print("Nem tudom értelmezni")