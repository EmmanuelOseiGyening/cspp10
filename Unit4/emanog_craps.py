import random

def instructions():
    
def get_player_bet():
    bet = int(input("How much would you like to bet?"))
    return bet
    
def dice_roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2 
    return ("You rolled {} and {}. The sum is {}".format(dice1,dice2,dice_sum))

def first_roll(dice_sum):
    if (dice_sum == 7) or (dice_sum == 11):
        return ("You won the roll")
    elif (dice_sum == 2) or (dice_sum == 3) or (dice_sum == 12):
        return ("You lose")
    else:
        return dice_sum

def get_or_lose_money(bet,dice_sum):
    if (dice_sum == 7) or (dice_sum == 11):
        bank = bet + bet
    elif (dice_sum == 2) or (dice_sum == 3) or (dice_sum == 12):
        bank = bet - bet 
    else:
        return ("It is time for Phase Three: Point Number")

def craps():
    print ("Welcome to The Wonderful Game of Craps")
    print (" ")
    
    bet = get_player_bet()
    dice_sum = dice_roll()
    
craps()