num_list = []

number_choice = 1
while number_choice != 0:
    number_choice = int(input ("Enter a number: "))
    
    if number_choice >= 1:
        num_list.insert(0, number_choice)
    
    if number_choice < 0:
        if (number_choice * -1) in num_list:
            num_list.remove(number_choice * -1)
    
    if number_choice == 0:
        print("End")


    print (num_list)