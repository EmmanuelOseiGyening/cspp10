import random

word = "Hello"

def scramble_word(word):
    word = word[1:4]
    print (word)
    
    y = word[1:4]
    y = list(word[1:4])
    
    
    random.shuffle(y)
    print (y)





def scrambler(word):
    
    word = scramble_word(word)


scrambler(word)