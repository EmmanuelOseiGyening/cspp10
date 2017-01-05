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
    
def get_player_bet(bank):
    print("You have ${} in your bank and can only bet up to half the amount you have in your bank each turn.".format(bank))
    while True:
        bet = int(input("How much would you like to bet?: "))
        b = bet 
        if b >= 1 and b <= bank :
            return bet
    
   
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
    
def point_round(dice_sum):
    while True:
        print("You previously rolled {} which is a point number. Now we will have to do phase 3!".format(dice_sum))
        dice3 = random.randint(1,6)
        dice4 = random.randint(1,6)
        pn_sum = dice3 + dice4
        pw = pn_sum
        print ("Your point number rolls are {} and {}. The sum is {}".format(dice3,dice4,pn_sum))
        if pn_sum == dice_sum:
            print ("You win the roll")
            return ("W")
        elif pn_sum == 7:
            print ("You lose the roll")
            return ("L")
   
   
def craps():
    
    bank = 2000
    
    print ("Welcome to The Wonderful Game of Craps")
    print(" ")
    game_rules()
    
    while bank > 0:
        bet = get_player_bet(bank)
    
        dice_sum = first_roll(dice_roll())
    
        pn_sum = point_round(dice_sum)
    
        x = dice_sum
        b = bet
        pw = pn_sum
        if x == "Win":
            bank = bank + b
            print ("You now have ${} in your bank.".format(bank))
            print (" ")
        elif x == "Lose":
            bank = bank - b
            print("You now have ${} in your bank.".format(bank))
            print (" ")
        elif pw == "W":
            bank = bank + b
            print ("You now have ${} in your bank.".format(bank))
            print (" ")
        elif pw == "L":
            bank = bank - b
            print ("You now have ${} in your bank.".format(bank))
            print (" ")

    

    
    
craps()