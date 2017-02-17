from pprint import pprint

dictionary = {}

def add(dictionary):
    key = input ("What key would you like to add to the dictionary?: ")
    value = input ("What value do you want the key to have?: ")
    
    dictionary[key] = value
    return dictionary

def remove_key(dictionary):
    remove = input ("Which key would you like to remove from the dictionary?: ")

    if remove in dictionary:
        del dictionary[remove]
    
    return dictionary

def update(dictionary):
   key = input ("What key do you want to add to the list?: ")
   value = input ("What value do you want the key to have?: ")
   
   if key not in dictionary:
       dictionary[key] = value

   return dictionary

def prettyprint(dictionary):
    pprint(dictionary)
    
    return dictionary

def exit(dictionary):
    print(dictionary)
    
    return dictionary

def dic(dictionary):
    
    choice = input ("What would you like to do with the list?: ")
    
    while choice != "exit":
        
        choice = input ("What would you like to do with the list?: ")
        
        if choice == "add" or choice == "Add":
            dictionary = add(dictionary)
    
        elif choice == "remove" or choice == "Remove":
            dictionary = remove_key(dictionary)
    
        elif choice == "update" or choice == "Update":
            dictionary = update(dictionary)
    
        elif choice == "print" or choice == "Print":
            dictionary = prettyprint(dictionary)
    
        elif choice == "exit" or choice == "Exit":
            dictionary = exit(dictionary)
    
    
dic(dictionary)



# add(dictionary)
# remove_key(dictionary)
# update(dictionary)
# prettyprint(dictionary)
# exit(dictionary)