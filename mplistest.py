# Tyler "Can't Code on his own" King worked with me
# continue_to_list = input(" Do you want to add mor  to the list?: ")

# while continue_to_list != "No":
#     if continue_to_list == "Yes":
#         input("What else do you want to add to the list? ")

mix_list = []

list_choice = "Nothing"

while list_choice != "Exit":
    list_choice = int(input("Enter a number: or Write an action to do with the list:"))
    
    if list_choice == "Sum" or list_choice == "sum":
        list_sum = 0
        for list_choice in mix_list:
            list_sum = list_choice + list_sum
        print (mix_list)
        print (list_sum)

    elif list_choice == "Clear" or list_choice == "clear":
        mix_list = []
        print (mix_list)
    
    elif list_choice == "Print" or list_choice == "print":
        print(mix_list)

    elif list_choice == "Length" or list_choice == "length":
        print(mix_list)
        print(len(mix_list))
    
    elif list_choice == "Exit" or list_choice == "exit":
        print("End")
        break
    else:
        if list_choice >= 0:
            mix_list.insert(0, list_choice)
        
