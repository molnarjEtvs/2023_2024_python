import random
def ipGen(db):
    ipcimek = []
    while len(ipcimek)<db:
        ip = ""
        for _ in range(4):
            szam = random.randint(0,255)
            ip += str(szam)+"."
        ip = ip[:-1]
        if ip not in ipcimek:
            ipcimek.append(ip)
    return ipcimek

cimek = ipGen(5)
print(cimek)