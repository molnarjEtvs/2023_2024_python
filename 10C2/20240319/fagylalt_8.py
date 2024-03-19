gombocokSzama = input("Add meg a gombócok számát: ")
gombocokSzama = int(gombocokSzama)

gombocAra = input("Add meg a gombóc árát: ")
gombocAra = int(gombocAra)

tolcserAra = input("Add meg a tölcsér árát: ")
tolcserAra = int(tolcserAra)

if gombocokSzama>3:
    tolcserAra = 0

fizetendo = (gombocokSzama*gombocAra)+tolcserAra
print(f"{gombocokSzama} gombóc fagylalt a tölcsérrel együtt {fizetendo} Ft lesz.")