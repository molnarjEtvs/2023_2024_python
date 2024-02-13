class Harcos:
    def __init__(self,nev,eletEro,harciEro):
        self.nev = nev
        self.eletEro = eletEro
        self.harciEro = harciEro
    
    def harcol(self,masikHarcos):
        self.eletEro -= masikHarcos.harciEro
        print(f"{harcos1.nev} eletereje csökkent, {harcos2.harciEro}")
        masikHarcos.eletEro -= self.harciEro
        print(f"{masikHarcos.nev} eletereje csökkent, {harcos2.harciEro}")
        if self.eletEro<=0 or masikHarcos.eletEro<=0:
            return True
        else:
            return False

harcos1 = Harcos("Chuck Noris",100,50)
harcos2 = Harcos("Rambo",100,40)

while True:
    eredmeny = harcos1.harcol(harcos2) 
    if eredmeny == True:
        break

print(f"{harcos1.nev}: {harcos1.eletEro}")
print(f"{harcos2.nev}: {harcos2.eletEro}")
if harcos1.eletEro>0:
    print(f"{harcos1.nev} nyert")
elif harcos2.eletEro>0:
    print(f"{harcos2.nev} nyert")
else:
    print("Mindkettő veszített")