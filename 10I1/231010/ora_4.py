import os 
os.system("cls")

szo = ""
while szo != "STOP":
    szo = input("Adj meg egy szót: ")
print("A program véget ért.")

#MÁSIK MEGOLDÁS

while True:
   szo = input("Adj meg egy szót: ")
   if szo == "STOP":
       break
print("A program véget ért.")