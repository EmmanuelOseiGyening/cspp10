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





def scrambler(word):
    
    word = scramble_word(word,x,y)


scrambler(word)