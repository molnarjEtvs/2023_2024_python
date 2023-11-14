
csunya = ["a","b","c"]
szep = ["x","y","z"]

mondat = input("Add meg a mondatot")

index = 0
for _ in csunya:
    mondat = mondat.replace(csunya[index],szep[index])
    index+=1
print(mondat)