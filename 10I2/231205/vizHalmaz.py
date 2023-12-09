import os
os.system("cls")

homerseklet = input("Add meg a víz hőmérsékletét: ")
homerseklet = int(homerseklet)

if homerseklet>=100:
    print("Gőz")
elif homerseklet<=0:
    print("Jég")
else:
    print("Folyékony")