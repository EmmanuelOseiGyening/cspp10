#Worked With Tyler 

original = [1,2,3,4,5,6,1,1,6,8,1]
to_replace = 1
replace_with = 6


def replace_all(original,to_replace,replace_with):
    for number in range(len(original)):
        if original[number] == to_replace:
            original[number] = replace_with


replace_all(original,to_replace,replace_with)

print(original)