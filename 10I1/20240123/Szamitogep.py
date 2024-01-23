class Szamitogep:
    def __init__(self,szabadTarhely,benvanEKapcsolva,azonosito):
        self.szabadTarhely = szabadTarhely
        self.benvanEKapcsolva = benvanEKapcsolva
        self.azonosito = azonosito

    def kapcsol(self):
        if self.benvanEKapcsolva == False:
            self.benvanEKapcsolva = True
        else:
            self.benvanEKapcsolva = False
    
    def programMasol(self,mb):
        if self.benvanEKapcsolva == True and self.szabadTarhely>=mb:
            self.szabadTarhely -= mb
            return True
        else:
            return False
    
szgep1 = Szamitogep(500,True,"123456")
szgep2 = Szamitogep(1000,False,"6456654")

sikeres = szgep1.programMasol(600)
if sikeres ==True:
    print("Másolás sikeres volt")
else:
    print("Sikertelen volt a másolás")