# Tyler "Can't Code on his own" King worked with me
# continue_to_list = input(" Do you want to add mor  to the list?: ")

# while continue_to_list != "No":
#     if continue_to_list == "Yes":
#         input("What else do you want to add to the list? ")

mix_list = []

list_action = "Nothing"

while list_action != "Exit":
    list_choice = int(input("Enter a number: "))
    list_action = input("What do you want to do with the list? ")
    
    if list_choice >= 0:
        mix_list.insert(0, list_choice)
    
    if list_action == "Sum" or list_action == "sum":
        list_sum = 0
        for list_choice in mix_list:
            list_sum = list_choice + list_sum
        print (mix_list)
        print (list_sum)

    elif list_action == "Clear" or list_action == "clear":
        mix_list = []
        print (mix_list)
    
    elif list_action == "Print" or list_action == "print":
        print(mix_list)

    elif list_action == "Length" or list_action == "length":
        print(mix_list)
        print(len(mix_list))
    
    elif list_action == "Exit" or list_action == "exit":
        print("End")
        break
