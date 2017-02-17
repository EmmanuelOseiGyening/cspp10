from pprint import pprint

dictionary = {}

def add(dictionary):
    key = input ("What key would you like to add to the dictionary?: ")
    value = input ("What value do you want the key to have?: ")
    
    dictionary[key] = value

def remove_key(dictionary):
    remove = input ("Which key would you like to remove from the dictionary?: ")

    if remove in dictionary:
        del dictionary[remove]

def update(dictionary):
   key = input ("What key do you want to add to the list?: ")
   value = input ("What value do you want the key to have?: ")
   
   if key not in dictionary:
       dictionary[key] = value

def prettyprint(dictionary):
    pprint(dictionary)

def exit(dictionary):
    print(dictionary)

def dictionary()



# add(dictionary)
# remove_key(dictionary)
# update(dictionary)
# prettyprint(dictionary)
# exit(dictionary)