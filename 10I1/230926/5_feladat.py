

for szam in range(1,51):
    if szam%5==0 and szam%3==0:
        print("Fizzbuzz")
    elif szam%3==0:
        print("Fizz")
    elif szam%5==0:
        print("Buzz")
    else:
        print(szam)