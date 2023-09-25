szam = input("Adj meg egy számot: ")
szam=int(szam)

if szam%3==0 and szam%4==0:
    print("3al és 4el is osztható")
elif szam%3==0:
    print("csak 3al")
elif szam%4==0:
    print("csak 4-el")
else:
    print("Egyikkel sem osztható")