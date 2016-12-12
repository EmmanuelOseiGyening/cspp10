import random

# def game_info():

def game_rules():
    i = input("Do you know how to play Craps? [Yes or No]: ")
    if i == "No" or  i == "no":
        print(" ")
        print("Phase 1: Before The Roll ")
        print("In this phase, the player has to make an accepted bet before the dice are rolled.")
        print(" ")
        print("Phase 2: The First Roll")
        print("When the first pair of dice are rolled, a few outcomes can happen based on the sum: ")
        print("If the player rolls a 2, 3, or 12 in this phase, they lose their bet, and the round ends.")
        print("If the player rolls a 7 or 11 in this phase, they win their bet, and the round ends.")
        print("If the player rolls any other number (a 4,5,6,8,9,10), then they continue to Phase 3, with their roll becoming their “point number“")
        print(" ")
        print("Phase 3: The Point Number")
        print("If the player reaches Phase 3, which most rounds they do, then they keep rolling die until they roll a 7 or they roll their point number.")
        print("If the player rolls their point number first, they win their bet, and the round ends.")
        print("If the player rolls a 7 first, they lose their bet, and the round ends.")
        print("If the player rolls any other number, they keep rolling in Phase 3.")
        print(" ")
    elif i == "Yes" or i == "yes":
        print("You may continue to the game!")
        print(" ")
    
def get_player_bet():
    while True:
        bet = int(input("How much would you like to bet?: "))
        if bet >= 50 and bet <= 100:
            return ("Try Again")
    
def dice_roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2 
    print ("You rolled {} and {}. The sum is {}".format(dice1,dice2,dice_sum))
    return dice_sum

def first_roll(dice_sum):
    if (dice_sum == 7) or (dice_sum == 11):
        print ("You won the roll")
    elif (dice_sum == 2) or (dice_sum == 3) or (dice_sum == 12):
        print ("You lose the roll")
    else:
        return dice_sum

# def get_or_lose_money(bet,dice_sum,bank):
#     if dice_sum == 7 or dice_sum == 11:
        
#     elif dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
#         bank = bet - bet
#         return bank
#     else:
#         print ("It is time for Phase Three: Point Number")

def point_number():
    

def craps():
    print ("Welcome to The Wonderful Game of Craps")
    print(" ")
    game_rules()
    
    bet = get_player_bet()
    
    dice_sum = first_roll(dice_roll())
    
    bank = get_or_lose_money(dice_sum,bet)
    
craps()