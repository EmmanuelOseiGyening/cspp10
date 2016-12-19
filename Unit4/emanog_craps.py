import random


# def game_info():

def game_rules():
    i = input("Do you know how to play Craps? [Yes or No]: ")
    if i == "No" or  i == "no" or i == "NO":
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
    elif i == "Yes" or i == "yes" or i == "YES":
        print("You may continue to the game!")
        print(" ")
    
def get_player_bet():
    print("You have $2000 in your bank and can only bet up to half the amount you have in your bank each turn, and no less than $100. ")
    while True:
        bet = int(input("How much would you like to bet?: "))
        b = bet 
        if b >= 100 and b <= 1000 :
            return ("Accepted Bet")
    
   
def dice_roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2 
    print ("You rolled {} and {}. The sum is {}".format(dice1,dice2,dice_sum))
    return dice_sum

def first_roll(dice_sum):
    x = dice_sum
    if (dice_sum == 7) or (dice_sum == 11):
        print ("You won the roll")
        return ("Win")
    elif (x == 2) or (x == 3) or (x == 12):
        print ("You lose the roll")
        return ("Lose")
    else:
        return dice_sum
    

#function name: point_round()
#   arguments: point_number 
#   purpose: to reroll the dice, to get the sum of the rerolled dice, and tell who won the roll(round) overall
#   returns: the sum of the rerolled dice, and tells who won the roll(round) overall
# point number
# if the roll is a 7 lose round

def point_round(point_number):
    roll = dice_roll()
    

def craps():
    
    bank = 2000
    house = 5000
    
    print ("Welcome to The Wonderful Game of Craps")
    print(" ")
    game_rules()
    
    bet = get_player_bet()
    
    dice_sum = first_roll(dice_roll())
    x = dice_sum
    b = bet
    if x == "Win":
        bank = bank + int(b)
        print ("Now you have {} in your bank.".format(bank))
    elif x == "Lose":
        bank = bank - int(b)
        print(" Now you have {} in your bank.".format(bank))

    
    
craps()