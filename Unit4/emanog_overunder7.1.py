import random

def dice_rolls():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2 
    print ("You rolled {} and {}. The sum is {}".format(dice1,dice2,dice_sum))
    return dice_sum
    
def get_range(dice_sum):
    if dice_sum == range(1,6):
        print ("Under 7")
        return "under7"
    elif dice_sum == 7:
        print ("Equals 7")
        return "equal7"
    else:
        print ("Over 7")
        return "over7"
        
def overunder_seven():
    
    dice_sum = dice_rolls()
    
    range = get_range(dice_sum)

overunder_seven()