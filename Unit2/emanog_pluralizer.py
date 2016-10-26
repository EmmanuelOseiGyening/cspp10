word = input("What is this?: ")
num = input("How many of it?: ")
number_infront = num
original_word = word

    
if number_infront == "1":
    print("1 " + original_word)
else:
    if original_word[-2:] == "fe":
        print(number_infront + " " + original_word[:-2] + "ves") 
        
    elif original_word[-2:] == "ay" or original_word[-2:] == "oy" or original_word[-2:] == "ey" or original_word[-2:] == "uy":
        print(number_infront + " " + original_word + "s")

    elif original_word[-1] == "y":
        print(number_infront + " " + original_word[:-1] + "ies")
 
    elif original_word[-2:] == "sh" or original_word[-2:] ==  "ch":
        print(number_infront + " " + original_word + "es")

    elif original_word[-2:] == "us":
        print(number_infront + " " + original_word[:-2] + "i")
    else: 
        print (number_infront + " " + original_word + "s")
    

