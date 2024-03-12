import random
def ipCimek(db):
    cimek = []
    while len(cimek)<db:
        ip = ""
        for _ in range(4):
            ip += str(random.randint(0,255))+"." 
        ip = ip[:-1]
        if ip not in cimek:
            cimek.append(ip)
    return cimek

ipk = ipCimek(5)
print(ipk)