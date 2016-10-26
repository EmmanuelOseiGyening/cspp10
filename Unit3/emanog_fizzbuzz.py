# final = ""
# inp = input("Enter a number or exit: ")
# while(inp != "exit"):
#     final = final + inp + " "
#     inp = input("Enter a number or exit: ")
# print(final)

# num = input("Enter a number: ")
# for num in list(range(1,1000,1)):
#     if num % 3 or num == "3":
#         print("fizz")
#     elif num % 5 or num == "5":
#         print("buzz")
#     elif num % 3 and num % 5:
#         print("fizzbuzz")

num = int(input("Enter a number: "))
for x in list(range(num,100)):
    if x % 3 == 0 or x == "3":
        print("fizz")
    elif x % 5 == 0 or x == "5":
        print("buzz")
    elif x % 3 and x % 5:
        print("fizzbuzz")