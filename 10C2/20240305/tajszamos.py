import random
def getTaj():
    tajaszam = ""
    for _ in range(3):
        szam = random.randint(0,999)
        if szam<10:
            tajaszam += "00"+str(szam)+" "
        elif szam<100:
            tajaszam += "0"+str(szam)+" "
        else:
            tajaszam += str(szam)+" "
    return tajaszam[:-1]

t = getTaj()
print(t)