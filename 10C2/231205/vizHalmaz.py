import os
os.system("cls")

vizHomersklet = input("Add meg a víz hőmérsékletét: ")
vizHomersklet = float(vizHomersklet)

if vizHomersklet>=100:
    print("Gőz")
elif vizHomersklet<=0:
    print("Jég")
else:
    print("Cseppfolyós")