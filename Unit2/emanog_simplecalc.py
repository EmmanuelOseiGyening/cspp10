sum = input("What do you want to calculate?:")
num_1 = int(sum[0])
num_2 = int(sum[2])
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
elif operator == "%":
    x = num_1 % num_2

print("The result is "+ str(x))