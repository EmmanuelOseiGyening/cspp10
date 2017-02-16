from pprint import pprint

d = {
    "name": "Eman",
    "birthmonth": "March",
    "birthyear": 2001
}

print(d['name'])

schedule = {
    "A": "Chemistry",
    "B": "English",
    "FRed": "Health",
    "FGrey": "Weight Room",
    "C": "Geometry",
    "D": "Global",
    "E": "Global"
}

#Only checks if it exsists as a KEY (not value)
if "E" not in schedule:
    print ("e is in schedule")
else:
    print ("is not in schedule")    
    
#If a value exsists

for key in schedule:
    print (schedule[key])
    
#Check value

for key in schedule:
    if schedule[key] == "Global":
        print ("exsits as a value")
        break
else: #This is read if the for loop doesn't break
    print ("is not a value")


#Delete a key

del schedule['D']



# add(dictionary)
# print(dictionary)
# remove_key(dictionary)
# print(dictionary)    