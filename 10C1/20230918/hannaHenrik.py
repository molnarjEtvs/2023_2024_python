import os
os.system("cls")

hannaValasz = input("Hanna jön ma kosarazni? ")
henrikValasz = input("Henrik jön ma kosarazni? ")

if hannaValasz == "igen" and henrikValasz == "igen":
    print("Mind a ketten jönnek kosarazni")
elif hannaValasz == "nem" and henrikValasz == "nem":
    print("Egyik sem jön kosarazni")
else:
    print("Csak egy jön kosarazni")
