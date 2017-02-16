import random

def dice_rolls():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    dice4 = random.randint(1,6)
    dice5 = random.randint(1,6)
    print ("You rolled: {}, {}, {}, {}, and {}.".format(dice1,dice2,dice3,dice4,dice5))
    
    dice_sum = dice1 + dice2 + dice3 + dice4 + dice5
    print ("The sum of your roll is {}.".format(dice_sum))
    print (" ")
    return dice_sum
    
# def reroll(dice1,dice2,dice3,dice4,dice5):
#     x = input ("Would you like to reroll the dice?: ")
    
#     if x == "Yes":
#         y = input ("Which dice would you like to reroll?: "
        
#         if y == "dice1":
#             dice1 = random.randint(1,6)
#             print ("Your new roll is {}.".format(dice1))
#             return dice1
#         elif y == "dice2":
#             dice2 = random.randint(1,6)
#             print ("Your new roll is {}.".format(dice2))
#             return dice2
#         elif y == "dice3":
#             dice3 = random.randint(1,6)
#             print ("Your new roll is {}.".format(dice3))
#             return dice3
#         elif y == "dice4":
#             dice4 = random.randint(1,6)
#             print ("Your new roll is {}.".format(dice4))
#             return dice4
#         elif y == "dice5":
#             dice5 = random.randint(1,6)
#             print ("Your new roll is {}.".format(dice5))
#             return dice5
#     else:
#         print ("You may continue")






def yahtzee():
    
    
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    dice4 = random.randint(1,6)
    dice5 = random.randint(1,6)
    
    dice_sum = dice_rolls()

    # dice_sum = reroll(dice1,dice2,dice3,dice4,dice5)
    
    x = input ("Would you like to reroll the dice?: ")
    
    while x == "Yes":
    
        for y in range(3):
            if (x == "Yes") or (x == "yes"):
                y = input ("Which dice would you like to reroll?: ")
        
                if y == "dice1":
                    dice1 = random.randint(1,6)
                    print ("Your new roll is {}.".format(dice1))
                elif y == "dice2":
                    dice2 = random.randint(1,6)
                    print ("Your new roll is {}.".format(dice2))
                elif y == "dice3":
                    dice3 = random.randint(1,6)
                    print ("Your new roll is {}.".format(dice3))
                elif y == "dice4":
                    dice4 = random.randint(1,6)
                    print ("Your new roll is {}.".format(dice4))
                elif y == "dice5":
                    dice5 = random.randint(1,6)
                    print ("Your new roll is {}.".format(dice5))
                elif y == "Done" or "done":
                    print ("Record your information on your Yahtzee game sheet, and the next player can roll their dice.") 
        break


yahtzee()