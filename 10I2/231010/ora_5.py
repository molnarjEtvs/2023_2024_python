
szo = input("Mi legyen szó? ")

db = input("Mennyiszer írjam ki? ")
db = int(db)

for sorszam in range(1,db+1):
    print(f"{sorszam}. {szo}")