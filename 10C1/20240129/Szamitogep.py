class szamitogep:
    def __init__(self,szabadTarhely,bekapcsolva,azonosito):
        self.szabadTarhely = szabadTarhely
        self.bekapcsolva = bekapcsolva
        self.azonosito = azonosito
    def kapcsol(self):
        if self.bekapcsolva == True:
            self.bekapcsolva = False

        else:
            self.bekapcsolva = True
    def programMasol(self,meret):
        if self.szabadTarhely > meret and self.bekapcsolva==True:
            self.szabadTarhely -= meret
            return True
        else:
            return False
        
katiGepe = szamitogep(900,False,"12")
szamitogep2 = szamitogep(100,False,"13")
        
katiGepe.kapcsol()
sikeres = katiGepe.programMasol(800)
if sikeres == True:
    print("A másolás sikeres volt")
else:
    print("A másolás sikertelen volt")
sikeres = katiGepe.programMasol(400)
if sikeres == True:
    print("A másolás sikeres volt")
else:
    print("A másolás sikertelen volt")
szamitogep2.kapcsol()
sikeres = szamitogep2.programMasol(1)
if sikeres == True:
    print("A másolás sikeres volt")
else:
    print("A másolás sikertelen volt")

        