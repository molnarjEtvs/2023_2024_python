
tipus = input("Hogy szeretnél váltani (FC/CF): ")
homersklet = input("Add meg az értéket: ")
homersklet = float(homersklet)

if tipus == "FC":
    #farenheit => celsius
    eredmeny = (5*(homersklet-32))/9
elif tipus == "CF":
    eredmeny = (9*homersklet+(32*5))/5
else:
    print("ezt nem tudom értelmezni")

print(f"Az eredmény: {eredmeny}")