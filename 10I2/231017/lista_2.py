import os
os.system("cls")

eletkorok = []
while True:
    kor = input("Adj meg egy életkort: ")
    kor = int(kor)
    if kor == 0:
        break
    else:
        eletkorok.append(kor)
print(eletkorok)

#MÁSIK MEGOLDÁS

eletkorok = []
kor = -1
while kor != 0:
    kor = input("Add meg egy életkort: ")
    kor = int(kor)
    if kor != 0:
        eletkorok.append(kor)
print(eletkorok)

