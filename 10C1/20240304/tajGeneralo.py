import random
def tajaszamGeneralas():
    tajszam = ""
    for _ in range(3):
        szam = random.randint(0,999)
        if szam<10:
            szam = "00"+str(szam)
        elif szam<100:
            szam = "0"+str(szam)
        else:
            szam = str(szam)
        tajszam += szam+" "
    tajszam = tajszam[:-1]
    return tajszam

taj = tajaszamGeneralas()
print(taj)