import random
end_num = input("What number do you want to end the range?: ")
print("The number is between 1 and {}.".format(end_num))
answer = random.randint(1, int(end_num))
num_guess = 0
guess = 0
while guess != answer:
    guess = int(input("What number do you think it is? "))
    num_guess = num_guess + 1
    if guess > answer:
        print("The Number You Guessed is Too High and Wrong")
    elif guess < answer:
        print("The Number You Guessed is Too Low and Wrong")
    elif guess == answer:
        print("You Got It Right")
print("You guessed the right number it was {}. It only took you {} tries.".format(answer,num_guess))