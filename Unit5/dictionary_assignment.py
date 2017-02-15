import random

dictionary = {
    
}

def add(dictionary):
    key = input ("What key would you like to add to the dictionary?: ")
    value = input ("What value do you want the key to have?: ")
    
    dictionary[key] = value

def remove_key(dictionary):
    remove = input ("Which key would you like to remove from the dictionary?: ")

    del dictionary[remove]



add(dictionary)
print(dictionary)
remove_key(dictionary)
print(dictionary)    