import random
def ipGeneralas(db):
    ipcimek = []
    while len(ipcimek)<db:
        ipCim = ""
        for _ in range(4):
            ipCim = ipCim+str(random.randint(0,255))+"."
        ipCim = ipCim[:-1]
        if ipCim not in ipcimek:
            ipcimek.append(ipCim)
    return ipcimek

cimek = ipGeneralas(10)
print(cimek)