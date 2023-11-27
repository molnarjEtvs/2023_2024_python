import os
os.system("cls")
'''
tanulok = [
    {'vnev':'Kovács',
     'knev':'Béla',
     'atlag':3.4},
    {'vnev':'Molnár',
     'knev':'Márton',
     'atlag':2.8}
]'''

tanulok = []

while True:
    vnev = input("Add meg a vezetéknevet: ")
    if vnev == "":
        break
    knev = input("Add meg a keresztnevet")
    atlag = input("Add meg az átlagot: ")
    atlag = float(atlag)
    tanulo = {}
    tanulo['vnev'] = vnev
    tanulo['knev'] = knev
    tanulo['atlag'] = atlag
    tanulok.append(tanulo)

print(tanulok)
