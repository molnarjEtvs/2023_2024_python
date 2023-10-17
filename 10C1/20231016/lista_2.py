
eletkorok = []
while True:
    eletkor = input("Adj meg egy életkort: ")
    eletkor = int(eletkor)
    if eletkor == 0:
        break
    eletkorok.append(eletkor)
print(eletkorok)


#MÁSIK MEGOLDÁS:
eletkorok = []
eletkor = 1
while eletkor != 0:
    eletkor = input("Adj meg egy életkort: ")
    eletkor = int(eletkor)
    if eletkor != 0:
        eletkorok.append(eletkor)
print(eletkorok)
