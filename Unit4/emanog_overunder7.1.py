import random

def game_rules():
    rules = input("Do you know how to play overunder7?: ")
    if rules == "No":
        print ("Here is how to play!")
        print (" ")
        print ("The player starts with $100.")
        print ("The player keeps playing this game until he/she runs out of money.")
        print ("The player’s bank is displayed for the user.")
        print ("The player then chooses a range to bet on.")
        print (" ")
        print ("Their options are: ")
        print ("Over 7 (wants to roll 8-12) - 1:1 payout")
        print ("Under 7 (wants to roll 2-6) - 1:1 payout")
        print ("Equal 7 (wants to roll  7) - 4:1 payout")
        print (" ")
        print ("After the player chooses a range to bet on, they choose their bet.")
        print ("They cannot bet more money than they have in the bank, they cannot bet a negative number, and they cannot bet a decimal amount.")
        print (" ")
        print ("Then two dice are rolled.")
        print ("If the player won, then they win their payout.")
        print ("If they lose, they lose their bet.")
        print ("The round ends, and a new round begins (if the player has enough money).")
        print (" ")
    else:
        print ("You can continue to game!")
        print (" ")

def get_bet(bank):
    print ("How much money would you like to bet?")
    while True:
        bet = int(input("Enter your bet: "))
        if (bet == bank) or (bet < bank):
            print ("You have bet ${} for this round.".format(bet))
            print (" ")
            return bet

def get_choice():
    print ("Choose what you think the range of the sum will be in: Over 7, Under 7 or Equal 7")
    choice = input("What will the range be in?: ")
    
    if choice == "Over 7":
        print ("You have chose that the sum will be {}.".format(choice))
        print (" ")
        return "over7"
    elif choice == "Under 7":
        print ("You have chose that the sum will be {}.".format(choice))
        print (" ")
        return "under7"
    elif choice == "Equal 7":
        print ("You have chose that the sum will be {}.".format(choice))
        print (" ")
        return "equal7"
    

def dice_rolls():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2 
    print ("You rolled {} and {}. The sum is {}".format(dice1,dice2,dice_sum))
    return dice_sum
    
def get_range(dice_sum):
    if dice_sum < 7:
        print ("Under 7")
        return "under7"
    elif dice_sum == 7:
        print ("Equals 7")
        return "equal7"
    elif dice_sum > 7:
        print ("Over 7")
        return "over7"
        
def overunder7():
    
    bank = 100
    
    rules = game_rules()
    
    choice = get_choice()
    
    bet = get_bet(bank)
    
    dice_sum = dice_rolls()
    
    range = get_range(dice_sum)
    
    if choice == range:
        print ("You won!")
        
        if choice == "equal 7":
            bank = bank + 4 * bet
            print ("You now have ${} in your bank.".format(bank))

        else:
            bank = bank + bet
            print ("You now have ${} in your bank.".format(bank))

    else:
        print ("Sorry You Lose!")
        bank = bank - bet
        print ("You now have ${} in your bank.".format(bank))

overunder7()