original = [1,2,3,4,5]
to_replace = 1
replace_with = 15

def replace_all(original,to_replace,replace_with):
    for item in range(len(original)):
        original[1] = replace_with
        del original[1]
        # original.append(replace_with)
print (original)

