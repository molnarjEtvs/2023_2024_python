import os
os.system("cls")

hofok = input("Add meg a víz hőmérsékletét: ")
hofok = int(hofok)

if hofok>=100:
    print("Gőz")
elif hofok<=0:
    print("Jég")
else:
    print("Cseppfolyós")