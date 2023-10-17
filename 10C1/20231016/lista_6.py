
paros = []
paratlanok = []
harommaloszhatoak = []

for x in range(1,101):
    if x%2==0:
        paros.append(x)
    else:
        paratlanok.append(x)
    
    if x%3==0:
        harommaloszhatoak.append(x)
print(paros)
print(paratlanok)
print(harommaloszhatoak)