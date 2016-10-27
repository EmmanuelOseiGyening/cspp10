num = int(input("Enter a number: "))
int = int(num)
for x in range(1,num + 1):
    if x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    elif x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    else:
        print(x)