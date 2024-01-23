class Macska:
    def __init__(self,nev,suly,ehesE):
        self.nev = nev
        self.suly = suly
        self.ehesE = ehesE
        print(f"Létrejött {self.nev} nevű macska")

    def eszik(self,etelMennyiseg):
        if self.ehesE == True:
            self.suly += etelMennyiseg
            self.ehesE = False
            print(f"{self.nev} nevű macska evett")
            return True
        else:
            print(f"{self.nev} nevű macska NEM evett")
            return False
        
    def futkos(self):
        self.suly -= 0.1
        print(f"{self.nev} nevű macska futkosott")
        if self.ehesE == False:
            self.ehesE = True
    
    def jelenlegiErtekek(self):
        print(f"Név: {self.nev}")
        print(f"Súly: {self.suly} kg")
        if self.ehesE == True:
            print("Éhes-e: Igen")
        else:
            print("Éhes-e: Nem")

macska1 = Macska("Garfield",8.5,True)
macska2 = Macska("Cirmi",3.9,False)
for x in range(10):
    macska1.futkos()
macska2.futkos()
macska1.eszik(1)
macska2.eszik(0.5)
macska1.jelenlegiErtekek()
macska2.jelenlegiErtekek()