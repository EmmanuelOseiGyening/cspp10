import random

# [1] Make a function for the certain part of the code you are working on (def scramble_word())
# [2] Make a variable that holds string
# [3] Turn the string into a list ---> You can do this by using the list(variable that holds the string) code
# [4] Single out the first and last character from the string ---> You can do this by using string indexing/slicing to get the certain characters you need from the string
# [4a] You can find the length of he string using len() to see how many ketters are in the string
# [4b] You can then use string slicing to only get the characters in between the first and last index
# [4b] Then you would need to set the new slicied string equal to the original variable
#                                       OR
# [4c] You can use string slicing or indexing to remove the first and last index and only leave the remaining characters
# You can do [4] before [3] or [3] before [4]
# [5] Scramble the remaining characters that are in the string ---> You can do this by using the list.shuffle() code
# [6] Print the shuffled string

import random

word = input("Enter a word: ")
x = word[0]
y = word[-1]

def scramble_word(word,x,y):
    word = word[1:-1]
    print (word)
    
    word = list(word)
    
    
    random.shuffle(word)
    print(word)
    
    scrambled_word = x + ''.join(word) + y
    print(scrambled_word)

scrambler(word)



# [1] Make a function for the certain part of the code you are working on (def scramble_phase())
# [2] Make a variable that holds the phrase
# [3] Turn the phrase into a list <--- You can do this by using list(variable)