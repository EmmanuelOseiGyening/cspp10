import random
#function name: get_p1_move
#   arguments: none
#   purpose: present player with options, use input() to get player move
#   returns: the player's move as either 'r', 'p', or 's'
def get_p1_move():
    p_choice = input("rock, paper or scissors? ")
    if p_choice == "rock":
        return "r"
    elif p_choice == "paper":
        return "p"
    elif p_choice == "scissors":
        return "s"

#function name: get_comp_move():
#   arguments: none
#   purpose: randomly generates the computer's move,
#            either 'r' 'p' or 's'
#   returns: the computer's randomly generated move
def get_comp_move():
    c_choice = random.randint(1,3)
    if c_choice == 1:
        return "r"
    elif c_choice == 2:
        return "p"
    elif c_choice == 3:
        return "s"

#function name: get_rounds
#   arguments: none
#   purpose: allows the user to choose a number of rounds from 1 to 9.
#   returns: the user-chosen number of rounds
def get_rounds():
    rounds = int(input("How many rounds would you like to play? (between 1 and 9): "))
    return rounds

#function name: get_round_winner
#   arguments: player move, computer move
#   purpose: based on the player and computer's move, determine
#            the winner or if it's a tie
#   returns: returns a string based on the following:
#               "player" if player won
#               "comp" if computer won
#               "tie" if it's a tie
def get_round_winner(p_choice, c_choice):
    if p_choice == c_choice:
        return "tie"
    elif p_choice == "r" and c_choice == "s":
        return "player"
    elif p_choice == "r" and c_choice == "p":
        return "comp"
    elif p_choice == "p" and c_choice == "r":
        return "player"
    elif p_choice == "p" and c_choice == "s":
        return "comp"
    elif p_choice == "s" and c_choice == "p":
        return "player"
    elif p_choice == "s" and c_choice == "r":
        return "comp"

#function name: get_full_move
#   arguments: a single letter move 'r','p', or 's'
#   purpose: returns the "full" word of a given move
#   returns: returns a string based on the following:
#               "Rock" if given "r"
#               "Paper" if given "p"
#               "Scissors" if given "s"
def get_full_move(shortmove):
    if (p_choice == "r") or (c_choice == "r"):
        return "Rock"
    elif (p_choice == "p") or (c_choice == "p"):
        return "Paper"
    elif (p_choice == "s") or (c_choice == "s"):
        return "Scissors"

#function name: print_score
#   arguments: player score, computer score, number of ties
#   purpose: prints the scoreboard
#   returns: none
def print_score(pscore, cscore, ties):
    pscore = 0
    cscore = 0
    ties = 0
    print(pscore)
    print(cscore)
    print(ties)
    return "The score is Player 1 {}, Player 2 {}, and {} ties.".format(pscore,cscore,ties)

# #function name: rps
# #   arguments: none
# #   purpose: the main game loop.  This should be the longest, using
# #               all the other functions to create RPS
# #   returns: none
def rps():
    return 1

#function name: tests
#   arguments: none
#   purpose: a place for you to write your tests.  replace 'rps' below
#               with 'tests' to run this function instead of the game loop
#   returns: none
def test():
    return 1

rps()