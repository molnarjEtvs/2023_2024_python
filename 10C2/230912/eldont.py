import os
os.system('cls')

valasz = input("Jó napod van-e?")
if valasz == "igen":
    print("Ez egy király nap!")
elif valasz == "nem":
    print("Ez egy szörnyű nap!")
else:
    print("Sajnos nem tudtam értelmezni")