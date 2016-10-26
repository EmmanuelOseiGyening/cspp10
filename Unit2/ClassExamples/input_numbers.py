# program will take in a bunch of numbers untill the user types "exit" and then prints out all the nmbers together

final = ""
inp = input("Enter a number or exit: ")
while(inp != "exit"):
    final = final + inp + " "
    inp = input("Enter a number or exit: ")
print(final)