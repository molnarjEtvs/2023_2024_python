import os
os.system("cls")

eletkorok = []
while True:
    eletkor = input("Add meg az életkort: ")
    eletkor = int(eletkor)
    if eletkor == 0:
        break
    else:
        eletkorok.append(eletkor)
print(eletkorok)

#MÁSIK MEGOLDÁS
eletkorok = []
eletkor = -1
while eletkor != 0:
    eletkor = input("Add meg az életkort: ")
    eletkor = int(eletkor)
    if eletkor != 0:
        eletkorok.append(eletkor)
print(eletkorok)



