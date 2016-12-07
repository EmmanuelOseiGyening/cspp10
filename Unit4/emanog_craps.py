import random

def get_player_bet():
    bet = int(input("How much would you lime to bet?: "))

def dice_roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2 
    print("You rolled {} {}".format(dice1,dice2))

def first_roll(dice_sum):
    if (dice_sum == 7) or (dice_sum == 11):
        return ("You won the roll")
    elif (dice_sum == 2) or (dice_sum == 3) or (dice_sum == 12):
        return ("You lose")
    else:
        return dice_sum

    
# def roll_result(bet,dice_sum):
#     new_amount = 0
#     if dice_sum == 2:
#         new_amount = bet - bet
#     elif dice_sum == 3:
#         new_amount = bet - bet
#     elif dice_sum == 12:
#         new_amount = bet - bet
#     elif dice_sum == 7:
#         new_amount = bet + bet
#     elif dice_sum == 11:
#         new_amount = bet + bet
#     else:
#         point_number(dice_sum)
