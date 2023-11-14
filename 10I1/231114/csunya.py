import os
os.system("cls")

cs = ["a","b","c"]
sz = ["x","y","z"]

mondat = input("Add meg a mondatot")

for x in range(0,len(cs)):
    mondat = mondat.replace(cs[x],sz[x])

print(mondat)