import random

userValasz = input("Add meg 1.Kő, 2.Papír, 3.Olló: ")
userValasz = int(userValasz)

gepValasz = random.randint(1,3)

#1-1, 2-2, 3-3
if gepValasz == userValasz: 
    print("DÖNTETLEN")
elif (gepValasz==1 and userValasz == 2) or (gepValasz == 2 and userValasz == 3) or (gepValasz == 3 and userValasz == 1):
    print("NYERTÉL")
elif (gepValasz==1 and userValasz == 3) or (gepValasz == 2 and userValasz == 1) or (gepValasz == 3 and userValasz == 2):
    print("VESZTETTÉL")