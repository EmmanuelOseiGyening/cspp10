sum = input("What do you want to calculate?:") #This allows someone to input something.
num_1 = int(sum[0]) #This takes the fist character in the word and turns it into an interger
num_2 = int(sum[2]) #This takes 
operator = sum[1]
x = 0

if operator == "+":
    x = num_1 + num_2
elif operator == "*":
    x = num_1 * num_2
elif operator == "-":
    x = num_1 - num_2
elif operator == "/":
    x = num_1 / num_2


print("The result is "+ str(x))