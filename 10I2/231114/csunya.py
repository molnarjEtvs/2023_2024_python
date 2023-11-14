import os
os.system("cls")

cs = ["a","b","c"]
sz = ["y","x","z"]

mondat = "a b vkármi c"

for x in range(len(cs)-1):
    mondat = mondat.replace(cs[x],sz[x])

print(mondat)