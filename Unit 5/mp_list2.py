# continue_to_list = input(" Do you want to add mor  to the list?: ")
# while continue_to_list != "No":
#     if continue_to_list == "Yes":
#         input("What else do you want to add to the list? ")

mix_list = []

list_choice = int(input("Enter a number: "))
list_action = input("What do you want to do with the list? ")
list_sum = 0

while list_action != "Exit":
    if list_action == "Sum" or list_action == "sum":
        # for mix_list in mix_list:
        #     list_sum = mix_list + list_sum
        #     print (list_sum)

    elif list_action == "Clear" or list_action == "clear":
        mix_list = []
        print (mix_list)
    
    elif list_action == "Print" or list_action == "print":
        print(mix_list)

    elif list_action == "Length" or list_action == "length":
        print(len(mix_list))
    
    # elif list_action == "Exit" or list_action == "exit":
    #     print("End")

    # else: 
    #     mix_list.append(0, list_choice)
