import os
os.system("cls")

hannaValasz = input("Hanna jön-e kosarazni? ")
henrikValasz = input("Henrik jön-e kosarazni? ")

if hannaValasz == "igen" and henrikValasz == "igen":
    print("Mind ketten jönnek")
elif hannaValasz == "nem" and henrikValasz == "nem":
    print("Egyik sem jön")
else:
    print("Csak egyik jön")