
for y in range(1,51):
    if y%3==0 and y%5==0:
        print("Fizzbuzz")
    elif y%3==0:
        print("Fizz")
    elif y%5==0:
        print("Buzz")
    else:
        print(y)