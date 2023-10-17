import os
os.system("cls")
eletkorok = []
while True:
    eletkor = input("Adj meg egy életkort: ")
    eletkor = int(eletkor)
    if eletkor == 0:
        break
    else:
        eletkorok.append(eletkor)
print(eletkorok)

#MÁSIK MEGOLDÁS
eletkor = -1
eletkorok = []
while eletkor != 0:
    eletkor = input("Adj meg egy életkort: ")
    eletkor = int(eletkor)
    if eletkor != 0:
        eletkorok.append(eletkor)
print(eletkorok)