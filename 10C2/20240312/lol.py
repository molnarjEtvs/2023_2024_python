class Champion:
    def __init__(self,nev,kepesseg,tPont):
        self.nev = nev
        self.kepesseg = kepesseg
        self.tPont = tPont

champions = []
f = open("lol.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    sor = sor.split("|")
    champion1 = Champion(sor[0],sor[1],int(sor[2]))
    champions.append(champion1)
    del champion1
f.close()


