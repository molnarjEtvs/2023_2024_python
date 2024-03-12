#011 456 992
import random
def tajGen():
    tajSzam = ""
    for _ in range(3):
        szam = random.randint(0,999)
        if szam<10:
            tajSzam += "00"+str(szam)+" "
        elif szam<100:
            tajSzam += "0"+str(szam)+" "
        else:
            tajSzam += str(szam)+" "
    tajSzam = tajSzam[:-1]
    return tajSzam

t = tajGen()
print(t)
t = tajGen()
print(t)