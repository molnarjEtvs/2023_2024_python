import os 
os.system("cls")

km = input("Add meg a km számot: ")
km = int(km)

arszaz = input("Add meg a 100km ti árat: ")
arszaz = int(arszaz)

utikoltseg = 0

for x in range(1,km+1):
    if x%4==0 and x%6==0:
        utikoltseg += (arszaz/100)*(x*2)
        #utikoltseg = utikoltseg+(arszaz/100)*(x*2)

    else:
        utikoltseg += (arszaz/100)*x
print(f"Az utiköltséged: {utikoltseg} Ft -ba kerül")