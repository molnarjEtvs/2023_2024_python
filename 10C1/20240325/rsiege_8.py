jatekos1 = input("Kérlek add meg az első játékos nevét: ")
jatekos1_rang = input("Kérlek add meg az első játékos rangját: ")
jatekos1_rang = int(jatekos1_rang)

jatekos2 = input("Kérlek add meg az második játékos nevét: ")
jatekos2_rang = input("Kérlek add meg az másoidk játékos rangját: ")
jatekos2_rang = int(jatekos2_rang)

if jatekos1_rang>jatekos2_rang:
    nyertes = jatekos1
    vesztes = jatekos2
elif jatekos1_rang<jatekos2_rang:
    nyertes = jatekos2
    vesztes = jatekos1
else:
    nyertes = "DÖNTETLEN"
    vesztes = "DÖNTETLEN"

print(f"A csata győztese: {nyertes}")
print(f"A csata vesztese: {vesztes}")
