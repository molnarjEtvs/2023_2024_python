import os
os.system("cls")

vegosszeg = 0
befizetes = 0


#B csop  befizetes != -2:
while befizetes!=-1:
    befizetes = input("Add meg a befizetés összege: ")
    befizetes = int(befizetes)
    if befizetes != -1:
        vegosszeg += befizetes
        
print(f"A gyüjtött összeg: {vegosszeg} Ft")