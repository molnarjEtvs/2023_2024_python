
def fagylaltNevek():
    fagyik = []
    while True:
        iz = input("Add meg a fagyi izét: ")
        if iz == "":
            break
        iz = iz.capitalize()
        fagyik.append(iz)
    return fagyik

def Statisztika(fagylaltok):
    db = len(fagylaltok)
    veganDb = 0
    print(f"{db} féle fagylalt van")
    for x in fagylaltok:
        if x.find("vegán")>-1 or x.find("Vegán")>-1:
            veganDb += 1
    print(f"Ebből vegán izesítésű: {veganDb} db")

f = fagylaltNevek()
Statisztika(f)

