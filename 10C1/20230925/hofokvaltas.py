
valasz = input("Add meg hogyan szertnél váltan (FC/CF): ")
homerseklet = input("Add meg a hőmérsékletet: ")
homerseklet = float(homerseklet)

if valasz == "FC":
    #Farenheit => Celsiusra
    #( 5 * ( F-32 ) ) / 9
    celsius = (5*(homerseklet-32)) /9
    print("Celsiusban ez {celsius}C fokot jelent")

elif valasz == "CF":
    #Celsiusra => Farenheit
    #F = (9 * C + (32 * 5) ) / 5
    farenheit = (9*homerseklet+(32*5))/5
    print(f"Fareinheitben a hőmérséklet: {farenheit} F")
else:
    print("Nem tudom értelmezni")
