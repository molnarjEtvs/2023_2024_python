import os 
os.system("cls")


szo = input("Add meg a szót: ")

db = input("Hányszor írjam ki: ")
db = int(db)

for x in range(1,db+1):
    print(f"{x}. {szo}")