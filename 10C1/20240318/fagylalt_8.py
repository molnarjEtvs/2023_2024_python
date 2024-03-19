gombocAr = input("Add meg mennyibe kerül egy gombóc fagyi?: ")
gombocAr = int(gombocAr)

hanyGomboc = input("Add meg a gombócok számát: ")
hanyGomboc = int(hanyGomboc)

tolcserAr = input("Add meg mennyibe kerül egy tölcsér?: ")
tolcserAr = int(tolcserAr)

if hanyGomboc>3:
    tolcserAr = 0

fizetendo = (hanyGomboc*gombocAr)+tolcserAr

print(f"{hanyGomboc} gombóc fagylalt a tölcsérrel együtt: {fizetendo} Ft lesz.")
